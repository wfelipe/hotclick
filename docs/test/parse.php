#!/usr/bin/php
<?
$logDir  = '/tmp';
$logFile = $logDir . '/access.log';
$fp      = fopen($logFile,"a+");
$stdin   = fopen("php://stdin", "r");

// Use unbuffered output
ob_implicit_flush (true);

while ($line = fgets($stdin))
{
   fwrite($fp, $line);
}

fclose($fd);
fclose($stdin);
?>
