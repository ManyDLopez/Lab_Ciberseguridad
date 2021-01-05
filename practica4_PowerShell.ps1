$puertos = Get-NetTCPConnection
foreach ($elemento in $puertos){
	if ($elemento.RemotePort -eq "80") {
		Write-Host $elemento.LocalAddress "is" $elemento.RemotePort -ForegroundColor yellow
	} elseif ($elemento.RemotePort -eq "443") {
		Write-Host $elemento.LocalAddress "is" $elemento.RemotePort -ForegroundColor Red
	}
}
