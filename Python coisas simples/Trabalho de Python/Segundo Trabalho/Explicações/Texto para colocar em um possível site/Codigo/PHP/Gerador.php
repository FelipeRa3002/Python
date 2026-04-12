<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST['nome'] ?? 'Sem Nome';
    $av = floatval($_POST['nota1'] ?? 0);
    $avs = floatval($_POST['nota2'] ?? 0);
    $decisao = $_POST['acao'] ?? '';

    salvamentodoDados($nome, $av, $avs, $decisao);
}

function salvamentodoDados($nome, $nota1, $nota2, $isagi) {
    $arquivo = 'dados.py';
    $media = ($nota1 + $nota2) / 2;
    $situacao = ($media >= 6) ? "Aprovado" : "Reprovado";

    $listaAtual = [];
    $mediadaTurmaDefinitiva = 0;

    // Se o arquivo existe, vamos extrair os dados atuais
    if (file_exists($arquivo)) {
        $conteudo = file_get_contents($arquivo);

        // 1. Extrai a lista do Python e converte para Array PHP
        if (preg_match('/listadaTurma\s*=\s*(\[[\s\S]*?\])/', $conteudo, $m)) {
            $jsonLimpo = str_replace("'", '"', $m[1]); // Troca ' por " para o JSON entender
            $jsonLimpo = preg_replace('/,\s*\]/', ']', $jsonLimpo); // Remove vírgula sobrando no final
            $listaAtual = json_decode($jsonLimpo, true) ?: [];
        }

        // 2. Extrai a média acumulada
        if (preg_match('/mediadaTurmaDefinitiva\s*=\s*([\d\.]+)/', $conteudo, $mMedia)) {
            $mediadaTurmaDefinitiva = floatval($mMedia[1]);
        }
    }

    // Adiciona o novo aluno ao array
    $listaAtual[] = [
        'nome' => $nome,
        'nota1' => $nota1,
        'nota2' => $nota2,
        'media' => $media,
        'situação' => $situacao
    ];

    // Atualiza a média total (soma das médias de todos os alunos)
    $mediadaTurmaDefinitiva += $media;

    // Reconstrói a string no formato EXATO do Python
    $pyLista = "listadaTurma = [\n";
    $controle = 1;
    foreach ($listaAtual as $aluno) {
        if($controle == 1){
           $pyLista .= "    {'nome': '{$aluno['nome']}', 'nota1': {$aluno['nota1']}, 'nota2': {$aluno['nota2']}, 'media': {$aluno['media']}, 'situação': '{$aluno['situação']}'}\n";
       }else{
        $pyLista .= " ,{'nome': '{$aluno['nome']}', 'nota1': {$aluno['nota1']}, 'nota2': {$aluno['nota2']}, 'media': {$aluno['media']}, 'situação': '{$aluno['situação']}'}\n";
       }
       $controle = $controle + 1
    }
    $pyLista .= "]\n";
    $pyLista .= "mediadaTurmaDefinitiva = $mediadaTurmaDefinitiva";

    // Salva no arquivo .py
    file_put_contents($arquivo, $pyLista);

    if ($isagi === "finalizar") {
        header('Content-Type: text/x-python');
        header('Content-Disposition: attachment; filename="dados.py"');
        echo $pyLista;
        exit;
    } else {
        echo "Dados salvos com sucesso! <br><a href='javascript:history.back()'>Voltar</a>";
    }
}
?>
