zkpwgen
=========
A tool for generating random passwords consisting of full-width Japanese and
Roman characters.

By default, generated passwords are intended to be easy to input on mobile
devices with a single conversion: a password contains *either* Hiragana or
Katakana, but not both. Same goes for upper- and lower-case Roman letters.

zkpwgen was heavily inspired by `pwgen <https://github.com/tytso/pwgen>`__. The
name is derived from *zenkaku* (全角, "full-width") *pwgen*.

Usage
=====
Example output::

    $ zkpwgen
    ギエカヘゴダピＯ ぁらみｘま８ぞｖ りかぱ２ゃｆょ８ モラ３ボ８メ１ズ
    メプヂＣゲペ６バ ゃ０ぉふ３ゅあ７ だ８へろＤせなＨ ジｂゲヒミカ４ツ
    ぅもふ２ゆｋけｓ ぢぁち６ぃへつＭ ヂ２ＦェＧサメベ ばそ８さＮてＧぼ
    ぎゆ８まほ５ｊば ぁぉばぱＨまＫず アｆベｕヒチゼｐ ヘテ４ラｖァ３ズ
    ノギＰガイルヅド ぜもぁ３あＧそＦ むどｇぽりｂてｇ ワモラセｅヒゴｈ
    ラＬモ５Ｌヨリ４ くぷあＤろ２ぐＨ ミ８ェジミマァテ よｂまｅぶはｌめ
    グ７ウィズスＰラ ば０ぶＯご２ゃた プ３ゴ７ョ１ュャ へ５ｃゎぽげ１が
    ぃＩするふどもＩ セテァプスキＮフ ス８ｍオ５ノ６ｇ ぜｕじ１ぇぎ０ｋ
    ぽだＯけれくＤぐ ッＯタ５ブゴ２ゾ ヮビワジ６フェｐ オダュ６Ｊベゼ６
    ゼＥナ４Ｏル３ュ ゥニヌ３ボヮャヲ て７ごしぺ８ぷけ つ７っ６Ａことゎ
    マリ５Ａレ８Ｐサ おみｗけ４ゎてｉ エ２サ８モエｆク どぅｇて４ｎぶ０
    まこさ４Ｉぜぺど ぷｔちひｓえぅげ ドｅゾ２ソヨｆニ トｘゲ０ノヒヌ０
    ゾグラ８ｋエユｔ だ３せ３ひ８ｙぞ マシクサヘコ６メ ばふさＨけじ７Ｈ
    チゼｊフメ４ｐオ リニｈクォ０ヒヌ ホベレ３ゲザＬア けｌぶ４ｒぐゃ８
    ァ４フ６ヒスズ０ ぎ７ゅＢと６こ７ ギ８エｐスｎムｏ フｒタｉツｎノ５
    へｎっｆゆｐぽり にＨう７ＥすＩく へｔめ８も８ｏぇ ぶぺぺ０ＩにろＥ
    らぬ６そ８ｍまゃ ぐ２れ７ｙぎあｔ し６な３ほ３Ｄす ヌＨトＯヘ１Ａツ
    ぐぐらぇは１ざ１ なっ４おぃ４う１ ぶぉ６ぷｒろ４い けＮぼよそへぃ６
    へげず６ゎべ５ゃ だ０ぴ０つ４だ７ ドセゴ４ネゥ７Ｅ うつゎ５Ｉうので
    ハ５ベケイ１Ｍス ォニケクポＤフズ ャＢホミ４シ２ル グッソ２ＨハボＤ

Invoke as :code:`zkpwgen -h` for help.

Quick Install
=============
This package is available from PyPI::

    pip install zkwgen

License
=======
zkpwgen is distributed under the `GPLv2 license <LICENSE>`__.
