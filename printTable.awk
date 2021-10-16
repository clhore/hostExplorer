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
        datos[vindex]["nombre"] = $1
        datos[vindex]["apellidos"] = $2
        datos[vindex]["ingreso"] = $3
}

END {

     for (i = 1; i <= vindex; i++){
        for (j = 1; j <= vindex-1; j++) {

                if (datos[j]["nombre"] > datos[j+1]["nombre"]){
                        c1 = datos[j+1]["nombre"]
                        c2 = datos[j+1]["apellidos"]
                        c3 = datos[j+1]["ingreso"]
                        datos[j+1]["nombre"] = datos[j]["nombre"]
                        datos[j+1]["apellidos"] = datos[j]["apellidos"]
                        datos[j+1]["ingreso"] = datos[j]["ingreso"]
                        datos[j]["nombre"] = c1
                        datos[j]["apellidos"] = c2
                        datos[j]["ingreso"] = c3
                }
        }
    }

    for (i = 1; i<=vindex; i++) {
    printf "| %-5s | %-17s| %-15s|\n", i, datos[i]["nombre"], datos[i]["apellidos"], datos[i]["ingreso"]
    }

    printf "%s \n", "+-------+------------------+----------------+"
    print VPIE
}
