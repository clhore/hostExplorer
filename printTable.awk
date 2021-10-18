BEGIN {
        FS=";"
	printf "%s \n", "+-------+------------------+----------------+"
        printf "|%-6s |%-18s| %-15s|\n", " Host ", "   IP Address   ", "System"
        printf "%s \n", "+-------+------------------+----------------+"
        vindex=0
        vsuma_salarios=0
}
{
        vindex++
        datos[vindex]["ip"] = $1
        datos[vindex]["system"] = $2
}

END {

     for (i = 1; i <= vindex; i++){
        for (j = 1; j <= vindex-1; j++) {

                if (datos[j]["ip"] > datos[j+1]["ip"]){
                        c1 = datos[j+1]["ip"]
                        c2 = datos[j+1]["system"]
                        datos[j+1]["ip"] = datos[j]["ip"]
                        datos[j+1]["system"] = datos[j]["system"]
                        datos[j]["ip"] = c1
                        datos[j]["system"] = c2
                }
        }
    }

    for (i = 1; i<=vindex; i++) {
    printf "| %-5s | %-17s| %-15s|\n", i, datos[i]["ip"], datos[i]["system"]
    }

    printf "%s \n", "+-------+------------------+----------------+"
    print VPIE
}
