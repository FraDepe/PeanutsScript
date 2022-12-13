#script per avviare lo scraper e mostrare l'immagine

script=`find $(dirname "$0") -name "peanuts.py"` 

python ${script}

img_folder=`find $HOME -name "Peanuts"`

img=`ls -Art ${img_folder} | tail -n 1`

img="${img_folder}/${img}"

echo "Loading image"

display ${img}&