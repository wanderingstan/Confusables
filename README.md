# 𝑪೦𝖓𝖋𝕦𝓼𝐚Б𝟭℮𝖘 (Confusables)
A simple Python 3 class for matching a strings that have letters that only *look* the same as original string. 

[unicode.org provides a list of "confusable" letters](http://www.unicode.org/Public/security/latest/confusables.txt).  This class uses that `confusables.txt` file to turn a string into a regular expression 
pattern that includes all these confusable variations.

E.g. "𝓗℮𝐥1೦" would match "Hello"

"Hello" gets turned into the following regex of character classes:


    [HＨℋℌℍ𝐇𝐻𝑯𝓗𝕳𝖧𝗛𝘏𝙃𝙷Η𝚮𝛨𝜢𝝜𝞖ⲎНᎻᕼꓧ𐋏ⱧҢĦӉӇ]  
    [e℮ｅℯⅇ𝐞𝑒𝒆𝓮𝔢𝕖𝖊𝖾𝗲𝘦𝙚𝚎ꬲеҽɇҿ]
    [l\u200e\\|∣⏽￨1\u200e۱𐌠\u200e𝟏𝟙𝟣𝟭𝟷IＩⅠℐℑ𝐈𝐼𝑰𝓘𝕀𝕴𝖨𝗜𝘐𝙄𝙸Ɩｌⅼℓ𝐥𝑙𝒍𝓁𝓵𝔩𝕝𝖑𝗅𝗹𝘭𝙡𝚕ǀΙ𝚰𝛪𝜤𝝞𝞘ⲒІӀ\u200e\u200e\u200e\u200e\u200e\u200e\u200e\u200eⵏᛁꓲ𖼨𐊊𐌉\u200e\u200ełɭƗƚɫ\u200e\u200e\u200e\u200eŀĿᒷ🄂⒈\u200e⒓㏫㋋㍤⒔㏬㍥⒕㏭㍦⒖㏮㍧⒗㏯㍨⒘㏰㍩⒙㏱㍪⒚㏲㍫ǉĲ‖∥Ⅱǁ\u200e𐆙⒒Ⅲ𐆘㏪㋊㍣Ю⒑㏩㋉㍢ʪ₶ⅣⅨɮʫ㏠㋀㍙]
    [l\u200e\\|∣⏽￨1\u200e۱𐌠\u200e𝟏𝟙𝟣𝟭𝟷IＩⅠℐℑ𝐈𝐼𝑰𝓘𝕀𝕴𝖨𝗜𝘐𝙄𝙸Ɩｌⅼℓ𝐥𝑙𝒍𝓁𝓵𝔩𝕝𝖑𝗅𝗹𝘭𝙡𝚕ǀΙ𝚰𝛪𝜤𝝞𝞘ⲒІӀ\u200e\u200e\u200e\u200e\u200e\u200e\u200e\u200eⵏᛁꓲ𖼨𐊊𐌉\u200e\u200ełɭƗƚɫ\u200e\u200e\u200e\u200eŀĿᒷ🄂⒈\u200e⒓㏫㋋㍤⒔㏬㍥⒕㏭㍦⒖㏮㍧⒗㏯㍨⒘㏰㍩⒙㏱㍪⒚㏲㍫ǉĲ‖∥Ⅱǁ\u200e𐆙⒒Ⅲ𐆘㏪㋊㍣Ю⒑㏩㋉㍢ʪ₶ⅣⅨɮʫ㏠㋀㍙]
    [oంಂംං०੦૦௦౦೦൦๐໐၀\u200e۵ｏℴ𝐨𝑜𝒐𝓸𝔬𝕠𝖔𝗈𝗼𝘰𝙤𝚘ᴏᴑꬽο𝛐𝜊𝝄𝝾𝞸σ𝛔𝜎𝝈𝞂𝞼ⲟоჿօ\u200e\u200e\u200e\u200e\u200e\u200e\u200e\u200e\u200e\u200e\u200e\u200e\u200e\u200e\u200e\u200e\u200e\u200e\u200e\u200eഠဝ𐓪𑣈𑣗𐐬\u200eøꬾɵꝋөѳꮎꮻꭴ\u200eơœɶ∞ꝏꚙൟတ]

(Note: Some characters above may not render in your browser correctly.)

Simple usage:
```
>>> from confusables import Confusables
>>> Confusables('confusables.txt').confusables_regex("A")
'[AＡ𝐀𝐴𝑨𝒜𝓐𝔄𝔸𝕬𝖠𝗔𝘈𝘼𝙰Α𝚨𝛢𝜜𝝖𝞐АᎪᗅꓮ𖽀𐊠ꜲÆӔꜴ🜇ꜶꜸꜺꜼ]'
```

It's probably best to combine this with removing accented characters in the text to be searched. Several ways explained here: https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string


Inspiration: https://stackoverflow.com/questions/9491890/is-there-a-list-of-characters-that-look-similar-to-english-letters/48555901#48555901
