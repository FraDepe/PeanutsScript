
main() {

    script_path=$1

    if [[ `which python` == *"/python" ]] 
    then
        python ${script_path}
    elif [[ `which python3` == *"/python3" ]]
    then
        python3 ${script_path}
    else
        echo "please install python or python3"
    fi
}

show(){     

    img_folder=$1

    img=`ls -t ${img_folder} | head -n 1`

    img="${img_folder}/${img}"

    echo "Loading image"

    if [[ `which display` == *"/display" ]] 
    then
        display ${img}&
    else
        echo "Please install display or choose a different command using -c option"
    fi

}

help() {

    # Display Help
    echo "Options to show or not downloaded image"
    echo "WIth no options will just download newer illustration"
    echo
    echo "Syntax: getPeanuts.sh [-s|h|c]"
    echo "options:"
    echo "s     Save and show latest illustration"
    echo "h     Print this Help"
    echo "c     Specify command to show image (default is display)"
    echo "d     Specify a date using format dd/mm/yyyy"
    echo

}

custom_show(){

    com=$1
    img_folder=$2

    img=`ls -t ${img_folder} | head -n 1`

    img="${img_folder}/${img}"

    echo "Loading image"

    entire_command="${com} ${img}&"

    eval "$entire_command"

}

getPath(){

    config_path=`find $(dirname $0) -name "peanuts_config.json"`

    path=`grep -o '"path": "[^"]*' $config_path | grep -o '[^"]*$'`

    echo ${path}

}

main_with_date(){
    
    script_path=$1
    date=$2

    if [[ `which python` == *"/python" ]] 
    then
        python ${script_path} ${date}
    elif [[ `which python3` == *"/python3" ]]
    then
        python3 ${script_path} ${date}
    else
        echo "please install python or python3"
    fi


}

script=`find $(dirname "$0") -name "peanuts.py"`
peanuts_folder=$(getPath)

while getopts ":h :s c: p: d:" option; do
    case $option in 
        h) # display Help
            help
            exit;;

        s) # Save and show latest illustration
            main "$script"
            show "$peanuts_folder"
            exit;;

        c) # Save and show latest illustration with the command specified
            command=$OPTARG
            main "$script"
            custom_show "$command" "$peanuts_folder"
            exit;;

        d)  # Download illustration of a specific date
            main_with_date "$script" "$OPTARG"
            exit;;

        \?) # Invalid option
            echo "Error: Invalid option"
            echo "Try using -h"
            exit;
   esac
done

main "$script" 
