# Confusables
Simple python 3 class for matching a strings that have letters that only 
*look* the same as original string. [unicode.org provides a nice list of 
"confusable" letters](http://www.unicode.org/Public/security/latest/confusables.txt).  
This class uses that info to turn a string into a regular expression 
pattern that includes all these confusable variations.

E.g. "𝓗℮𝐥1೦" matches "Hello"

"Hello" gets turned into the following regex of character classes:

    [H\Ｈ\ℋ\ℌ\ℍ\𝐇\𝐻\𝑯\𝓗\𝕳\𝖧\𝗛\𝘏\𝙃\𝙷\Η\𝚮\𝛨\𝜢\𝝜\𝞖\Ⲏ\Н\Ꮋ\ᕼ\ꓧ\𐋏\Ⱨ\Ң\Ħ\Ӊ\Ӈ]
    [e\℮\ｅ\ℯ\ⅇ\𝐞\𝑒\𝒆\𝓮\𝔢\𝕖\𝖊\𝖾\𝗲\𝘦\𝙚\𝚎\ꬲ\е\ҽ\ɇ\ҿ]
    [l\‎\|\∣\⏽\￨1\‎\۱\𐌠\‎\𝟏\𝟙\𝟣\𝟭\𝟷I\Ｉ\Ⅰ\ℐ\ℑ\𝐈\𝐼\𝑰\𝓘\𝕀\𝕴\𝖨\𝗜\𝘐\𝙄\𝙸\Ɩ\ｌ\ⅼ\ℓ\𝐥\𝑙\𝒍\𝓁\𝓵\𝔩\𝕝\𝖑\𝗅\𝗹\𝘭\𝙡\𝚕\ǀ\Ι\𝚰\𝛪\𝜤\𝝞\𝞘\Ⲓ\І\Ӏ\‎\‎\‎\‎\‎\‎\‎\‎\ⵏ\ᛁ\ꓲ\𖼨\𐊊\𐌉\‎\‎\ł\ɭ\Ɨ\ƚ\ɫ\‎\‎\‎\‎\ŀ\Ŀ\ᒷ\🄂\⒈\‎\⒓\㏫\㋋\㍤\⒔\㏬\㍥\⒕\㏭\㍦\⒖\㏮\㍧\⒗\㏯\㍨\⒘\㏰\㍩\⒙\㏱\㍪\⒚\㏲\㍫\ǉ\Ĳ\‖\∥\Ⅱ\ǁ\‎\𐆙\⒒\Ⅲ\𐆘\㏪\㋊\㍣\Ю\⒑\㏩\㋉\㍢\ʪ\₶\Ⅳ\Ⅸ\ɮ\ʫ\㏠\㋀\㍙]
    [l\‎\|\∣\⏽\￨1\‎\۱\𐌠\‎\𝟏\𝟙\𝟣\𝟭\𝟷I\Ｉ\Ⅰ\ℐ\ℑ\𝐈\𝐼\𝑰\𝓘\𝕀\𝕴\𝖨\𝗜\𝘐\𝙄\𝙸\Ɩ\ｌ\ⅼ\ℓ\𝐥\𝑙\𝒍\𝓁\𝓵\𝔩\𝕝\𝖑\𝗅\𝗹\𝘭\𝙡\𝚕\ǀ\Ι\𝚰\𝛪\𝜤\𝝞\𝞘\Ⲓ\І\Ӏ\‎\‎\‎\‎\‎\‎\‎\‎\ⵏ\ᛁ\ꓲ\𖼨\𐊊\𐌉\‎\‎\ł\ɭ\Ɨ\ƚ\ɫ\‎\‎\‎\‎\ŀ\Ŀ\ᒷ\🄂\⒈\‎\⒓\㏫\㋋\㍤\⒔\㏬\㍥\⒕\㏭\㍦\⒖\㏮\㍧\⒗\㏯\㍨\⒘\㏰\㍩\⒙\㏱\㍪\⒚\㏲\㍫\ǉ\Ĳ\‖\∥\Ⅱ\ǁ\‎\𐆙\⒒\Ⅲ\𐆘\㏪\㋊\㍣\Ю\⒑\㏩\㋉\㍢\ʪ\₶\Ⅳ\Ⅸ\ɮ\ʫ\㏠\㋀\㍙]
    [o\ం\ಂ\ം\ං\०\੦\૦\௦\౦\೦\൦\๐\໐\၀\‎\۵\ｏ\ℴ\𝐨\𝑜\𝒐\𝓸\𝔬\𝕠\𝖔\𝗈\𝗼\𝘰\𝙤\𝚘\ᴏ\ᴑ\ꬽ\ο\𝛐\𝜊\𝝄\𝝾\𝞸\σ\𝛔\𝜎\𝝈\𝞂\𝞼\ⲟ\о\ჿ\օ\‎\‎\‎\‎\‎\‎\‎\‎\‎\‎\‎\‎\‎\‎\‎\‎\‎\‎\‎\‎\ഠ\ဝ\𐓪\𑣈\𑣗\𐐬\‎\ø\ꬾ\ɵ\ꝋ\ө\ѳ\ꮎ\ꮻ\ꭴ\‎\ơ\œ\ɶ\∞\ꝏ\ꚙ\ൟ\တ]

Note: Some characters above may not render in your browser correctly. 

Probably best to combine this with removing accented characters in the text to be searched. Several ways explained here: https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string


Inspiration: https://stackoverflow.com/questions/9491890/is-there-a-list-of-characters-that-look-similar-to-english-letters/48555901#48555901
