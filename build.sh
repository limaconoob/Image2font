# Dont forget exports
make build run
docker cp $IMAGE $(make get):/root/image2font/$IMAGE
docker cp $FONT_INPUT $(make get):/root/image2font/$FONT_INPUT
docker exec $(make get) python image2font --input-font $FONT_INPUT --output-font $FONT_OUTPUT --start-index $INDEX $IMAGE
docker cp $(make get):/root/image2font/$FONT_OUTPUT $FONT_OUTPUT
