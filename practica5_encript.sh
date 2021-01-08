#!bin/bash

function descode {
echo 'ingrese el path del archivo'
read path

echo 'desea guradar como png o txt: '
read ext

if [[ "$ext" != "png" && "$ext" != "txt" ]]; then
	echo 'error'
else
	filname="${path##*/}"
	filname2="${filname%.*}"
	cat $path | base64 --decode > "$filname2 descode.$ext"
fi
}

function encode {
echo 'ingrese el path que desee decodificar'
read path

echo 'desea guardar como archivo png o txt: '
read ext

if [[ "$ext" != "png" && "$ext" != "txt" ]]; then
	echo'error'
else
	filname="${path##*/}"
	filname="${filname%.*}"
	cat $path | base64 > "$filname2 encode.$ext"
fi

}
echo '1-Codificar'
echo '2-Descodificar'
echo 'Salir'
read opcion

if ["$opcion" == "1"];
then
	encode
elif ["$opcion" == "1"];
then
	descode
else
	exit
fi
function md {
	md5sum /root/Descargas/mystery_img1.txt
	md5sum /root/Descargas/mysteryimg2.txt
	md5sum /root/Descargas/fcfm.png
	md5sum /root/Descargas/msg.txt
}
md
