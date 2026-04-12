<?php
// Força o PHP a mostrar qualquer erro que aconteça
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST['nome'] ?? 'Sem Nome';
    $av = floatval($_POST['nota1'] ?? 0);
    $avs = floatval($_POST['nota2'] ?? 0);
    $decisao = $_POST['acao'] ?? '';

    salvamentodoDados($nome, $av, $avs, $decisao);
}

function salvamentodoDados($x, $y, $z, $isagi) {
    $arquivo = 'dados.py';
    $media = floatval(($y + $z) / 2);
    $situacao = ($media >= 6) ? "\033[34mAPROVADO\033[0m" : "\033[31mREPROVADO\033[0m";

    $listaAtual = [];
    $mediadaTurmaDefinitiva = 0;

    // Se o arquivo não existe, vamos tentar criar um básico
    if (!file_exists($arquivo)) {
        file_put_contents($arquivo, "listadaTurma = []\nmediadaTurmaDefinitiva = 0");
    }

    $conteudo = file_get_contents($arquivo);

    // Captura a lista
    if (preg_match('/listadaTurma\s*=\s*(\[.*?\])/s', $conteudo, $m)) {
        $listaAtual = json_decode($m[1], true) ?: [];
    }

    // Captura a média acumulada
    if (preg_match('/mediadaTurmaDefinitiva\s*=\s*([\d\.]+)/', $conteudo, $mMedia)) {
        $mediadaTurmaDefinitiva = floatval($mMedia[1]);
    }

    // Adiciona novo dado e soma média
    $listaAtual[] = ["nome" => $x, "nota1" => $y, "nota2" => $z, "media" => $media, "situação" => $situacao];
    $mediadaTurmaDefinitiva += $media;

    // Prepara o conteúdo final
    $jsonLista = json_encode($listaAtual, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
    $conteudoFinal = "listadaTurma = " . $jsonLista . "\nmediadaTurmaDefinitiva = " . $mediadaTurmaDefinitiva;

    // Tenta salvar
    if (file_put_contents($arquivo, $conteudoFinal) === false) {
        die("ERRO: Não foi possível escrever no arquivo dados.py. Verifique as permissões da pasta.");
    }

    if ($isagi === "finalizar") {
        ob_clean();
        header('Content-Type: text/x-python');
        header('Content-Disposition: attachment; filename="dados.py"');
        header('Content-Length: ' . strlen($conteudoFinal));
        echo $conteudoFinal;
        exit;
    } else {
        echo "Dados salvos com sucesso! <a href='javascript:history.back()'>Voltar</a>";
    }
}
?>
