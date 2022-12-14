#script per avviare lo scraper e mostrare l'immagine
main() {
    script_name=$1

    python ${script} 
}

main_custom_path() {
    script_name=$1

    python ${script} $2
}

show(){

    img_folder=$1

    img=`ls -Art ${img_folder} | tail -n 1`

    img="${img_folder}/${img}"

    echo "Loading image"

    display ${img}&

}

help() {

    # Display Help
    echo "Options to show or not downloaded image"
    echo
    echo "Syntax: getPeanuts.sh [-s|h|c|p]"
    echo "options:"
    echo "s     Save and show latest illustration."
    echo "h     Print this Help."
    echo "c     Specify commanf to show iamge (default is display)."
    echo "p     Specify path (absolute) where to download image"
    echo "WIth no options will just download newer illustration"
    echo

}

custom_show(){

    com=$1
    img_folder=$2

    img=`ls -Art ${img_folder} | tail -n 1`

    img="${img_folder}/${img}"

    echo "Loading image"

    entire_command="${com} ${img}&"

    eval "$entire_command"


}

script=`find $(dirname "$0") -name "peanuts.py"`
peanuts_folder=`find $HOME -name "Peanuts"`

while getopts ":h :s c: p:" option; do
    case $option in 
        h) # display Help
            help
            exit;;
        s) # Save and show latest illustration
            main "$script"
            show "$peanuts_folder"
            exit;;
        c) 
            command=$OPTARG
            main "$script"
            custom_show "$command" "$peanuts_folder"
            exit;;
        p) 
            path=$OPTARG
            main_custom_path "$script" $path
            exit;;
        \?) # Invalid option
            echo "Error: Invalid option"
            echo "Try using -h"
            exit;
   esac
done

main "$script" 