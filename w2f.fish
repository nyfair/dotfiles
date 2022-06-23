function w2f
	for i in **.wav **.WAV
		ffmpeg -i (realpath $i) -compression_level 8 (string replace -r -i 'wav$' 'flac' (realpath $i)) 
		rm -f $i
	end
end