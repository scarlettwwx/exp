<?php
$post_data = json_decode(file_get_contents('php://input'), true); 
// the directory "data" must be writable by the server, use my github repo or local?
$name = "https://scarlettwwx.github.io/".$post_data['filename'].".csv"; 
$data = $post_data['filedata'];
// write the file to disk/directory
file_put_contents($name, $data);
?>