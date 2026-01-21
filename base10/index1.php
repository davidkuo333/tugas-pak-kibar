<?php

function cek_data($data){
    if(isset($_GET[$data])){
        if($_GET[$data] == null){
            return 0;
        }else{
            return $_GET[$data];
        }
    }else{
        return 0;
    }
}

$a = cek_data('angka1');
$b = cek_data('angka2');
function tambah($a, $b){
    return $a + $b;
}

function mines($a, $b){
    return $a - $b;
}

function kali($a, $b){
    return $a * $b;
}

function bagi($a, $b){
    if ($b == 0) {
        return "tidak bisa dibagi 0";
    }
    return $a / $b;
}

?>

<html>
    <head>
        <title>Operasi</title>
    </head>
    <body>
        <h2>hasil tambah : <?php echo tambah($a, $b); ?></h2>
        <h2>hasil mines : <?php echo mines($a, $b); ?></h2>
        <h2>hasil kali : <?php echo kali($a, $b); ?></h2>
        <h2>hasil bagi : <?php echo bagi($a, $b); ?></h2>
        <form action="" method="get">
            <label>Angka 1</label>
            <input type="number" name="angka1"><br>
            <label>Angka 2</label>
            <input type="number" name="angka2"><br>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>