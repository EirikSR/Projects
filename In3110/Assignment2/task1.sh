
Wd="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
Wd+="/"
#Setting up the environment, added / 

src=$1
echo $src
lst=() #List to check if two paths are suplied

if [ -d "$Wd$src" ]; then #checks if directory exists, either prompts rewrite or accepts
    echo "Directory $Wd$src exists."
    lst+=("$Wd$src")
else
    while [ ! -d "$Wd$src" ]; do
        echo "Directory $Wd$src does not exist, pleace reenter source folder. Write abort to abort"
        read src2
        if [ "$src2" == "abort" ]; then #Either quits program or restarts
            exit
        else
            echo "Enter source directory (relative to work directory)"
            src=$src2
        fi
    done
    lst+=("$Wd$src")
fi

#
#read dst
dst=$2
if [ -d "$Wd$dst" ]; then
    echo "Directory $Wd$dst exists."
    lst+=("$Wd$dst")
else
    while [ ! -d "$Wd$dst" ]; do
        printf "\nDirectory $Wd$dst does not exist,\n1 to create folder with same name as input ($dst)\n2 for new folder with date-time name\n3 to retry\n4 to abort\n"
        read dst2
        if [ "$dst2" == "1" ]; then
            mkdir $Wd$dst #creates directory with input as name
            echo "$Wd$dst created"
            dst=$dst2
            lst+=("$Wd$dst")
        elif [ "$dst2" == "2" ]; then
            DATE=$(date '+%Y-%m-%d-%H:%M:%S') #Gets date to create folder
            mkdir "$DATE"
            echo "$DATE created"
            dst="$DATE"
            lst+=("$Wd$dst")
        elif [ "$dst2" == "3" ]; then
            echo "Enter target directory (relative to work directory)"
            read dst3
            dst=$dst3
        elif [ "$dst2" == "4" ]; then
            echo "aborting"
            exit
        fi
    done
    lst+=("$Wd$dst")
fi


if [ "${#lst[@]}" == "2" ]; then #tests length of list
    echo "Select filetype to be transferred ('all' or specify file type without '.')"
    read FileT

    if [ "$FileT" == "all" ]; then #moves all files
        echo "Moving from" ${lst[0]} "to" ${lst[1]}
        mv $src/* $dst -i
    else                            #moves files with specific file ending
        echo "Moving from" ${lst[0]} "to" ${lst[1]}
        mv $src/*.$FileT $dst -i
    fi
fi