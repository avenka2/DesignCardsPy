from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
import concurrent.futures


class CardInfo:
    def __init__(self, yoga, color, number, title, vno, vdesc, sanskrit):
        self.yoga = yoga
        self.color = color
        self.number = number
        self.title = title
        self.vno = vno
        self.vdesc = vdesc
        self.sanskrit = sanskrit

card_deck = [
CardInfo("Jnana Yoga","Yellow","0","ignorance","2.42,2.43","lost in misunderstanding, many are: Crave for fame, power, gold and sense pleasures in exhchange for rituals the books prescribe, but miss the deeper truth they hide. Through wisdom and compassion, the truth we connect, not through passion and selfish effect.","यामिमां पुष्पितां वाचं प्रवदन्त्यविपश्चित: | वेदवादरता: पार्थ नान्यदस्तीति वादिन: || कामात्मान: स्वर्गपरा जन्मकर्मफलप्रदाम् | क्रियाविशेषबहुलां भोगैश्वर्यगतिं प्रति ||"),
CardInfo("Jnana Yoga","Yellow","1","Samsara","2.63","Anger clouds the mind. Truth hidden, memories fades, shattered is intellect. With no intellect, ruin awaits the angry one.","क्रोधाद्भवति सम्मोह: सम्मोहात्स्मृतिविभ्रम: | स्मृतिभ्रंशाद् बुद्धिनाशो बुद्धिनाशात्प्रणश्यति ||"),
CardInfo("Jnana Yoga","Yellow","2","Seeking","3.36","Arjun asked: Why is a person impelled to commit sinful acts, even unwillingly, as if by force, O descendent of Vrishni (Krishna)?","अथ केन प्रयुक्तोऽयं पापं चरति पूरुष: | अनिच्छन्नपि वार्ष्णेय बलादिव नियोजित: ||"),
CardInfo("Jnana Yoga","Yellow","3","Guru","4.34","to learn the truth, a spiritual master can help. Approach them with respect, young one. Serve them with humility, for wisdom they possess. Seen the Truth, they have. Share it, they can, if open your mind is","तद्विद्धि प्रणिपातेन परिप्रश्नेन सेवया | उपदेक्ष्यन्ति ते ज्ञानं ज्ञानिनस्तत्त्वदर्शिन: ||"),
CardInfo("Jnana Yoga","Yellow","4","Purification","13.8,13.9","cultivate these you must, for divine knowledge they bring purifies one like none: humility, truthfulness, harmlessness, forgiveness, simple ways. Serve your teacher well, young one. Cleanse body and mind. Steadfast be, and control your desires. ","अमानित्वमदम्भित्वमहिंसा क्षान्तिरार्जवम् | आचार्योपासनं शौचं स्थैर्यमात्मविनिग्रह: || इन्द्रियार्थेषु वैराग्यमनहङ्कार एव च | जन्ममृत्युजराव्याधिदु:खदोषानुदर्शनम् || "),
CardInfo("Jnana Yoga","Yellow","5","Viveka","2.16","The unreal has no existance, the real has no non-existance. Seen the final truth of these two, have those who pierced the veil of ignorance.","नासतो विद्यते भावो नाभावो विद्यते सत: | उभयोरपि दृष्टोऽन्तस्त्वनयोस्तत्त्वदर्शिभि: ||"),
CardInfo("Jnana Yoga","Yellow","6","Vairagya","2.58","Achieved stabilized wisdom one has, when like a turtle withdraws its limbs into its shell, senses from their temptations one withdraws. ","यदा संहरते चायं कूर्मोऽङ्गानीव सर्वश: | इन्द्रियाणीन्द्रियार्थेभ्यस्तस्य प्रज्ञा प्रतिष्ठिता ||"),
CardInfo("Jnana Yoga","Yellow","7","Go Deeper","15.3,15.4","Perceive the truth, one cannot like of banyan tree. Its beginning, end, nor existence continuous. With detachment's axe, cut one must, this deep-rooted tree. Then seek the base to find the suprement one from whom the universe emerged. After this, return to this illusion, one will not.","न रूपमस्येह तथोपलभ्यतेनान्तो न चादिर्न च सम्प्रतिष्ठा | अश्वत्थमेनं सुविरूढमूलमसङ्गशस्त्रेण दृढेन छित्त्वा || तत: पदं तत्परिमार्गितव्यं यस्मिन्गता न निवर्तन्ति भूय: | तमेव चाद्यं पुरुषं प्रपद्येयत: प्रवृत्ति: प्रसृता पुराणी ||"),
CardInfo("Jnana Yoga","Yellow","8","Theory","4.32","Upanishads speak the truth in numerous ways. Understand it you must, to cut through the knots of ignorance.","एवं बहुविधा यज्ञा वितता ब्रह्मणो मुखे | कर्मजान्विद्धि तान्सर्वानेवं ज्ञात्वा विमोक्ष्यसे ||"),
CardInfo("Jnana Yoga","Yellow","9","wisdom","13.2,13.3","A changing field of activities, the body-mind is, and the knower of this field, the soul is. O Scion, in all these fields, there is only one knower who I am. Final truth this I hold.","इदं शरीरं कौन्तेय क्षेत्रमित्यभिधीयते | एतद्यो वेत्ति तं प्राहु: क्षेत्रज्ञ इति तद्विद: || क्षेत्रज्ञं चापि मां विद्धि सर्वक्षेत्रेषु भारत | क्षेत्रक्षेत्रज्ञयोर्ज्ञानं यत्तज्ज्ञानं मतं मम ||"),
CardInfo("Jnana Yoga","Yellow","10","Enlightenment","13.24","Those who understand the truth about Supreme Soul, the individual soul, material nature, and the interaction of the three modes of nature will suffer no longer. Liberated are they, regardless of their condition.","य एवं वेत्ति पुरुषं प्रकृतिं च गुणै: सह | सर्वथा वर्तमानोऽपि न स भूयोऽभिजायते ||"),
CardInfo("Jnana Yoga","Yellow","0","ignorance","14.18","Upward rise those in knowledge, stagnant the passionate stay, downward the ignorant fall.","ऊर्ध्वं गच्छन्ति सत्त्वस्था मध्ये तिष्ठन्ति राजसा: | जघन्यगुणवृत्तिस्था अधो गच्छन्ति तामसा: ||"),
CardInfo("Jnana Yoga","Yellow","1","Samsara","18.38","Fleeting perceptions of happiness and distress, contact between the senses and world gives rise. Come and go like changing seasoons these don’t last. Sweet it seems, but bitter in the end.","विषयेन्द्रियसंयोगाद्यत्तदग्रेऽमृतोपमम् | परिणामे विषमिव तत्सुखं राजसं स्मृतम् ||"),
CardInfo("Jnana Yoga","Yellow","2","Seeking","2.54","Arjun asked: How does an enlightened person talk? How does he sit? How does he walk?","स्थितप्रज्ञस्य का भाषा समाधिस्थस्य केशव | स्थितधी: किं प्रभाषेत किमासीत व्रजेत किम् ||"),
CardInfo("Jnana Yoga","Yellow","3","Guru","6.43","Walk the path of Yog who does, reawakens the force of wisdom from past lives and strives even harder toward perfection in Yog. ","तत्र तं बुद्धिसंयोगं लभते पौर्वदेहिकम् | यतते च ततो भूय: संसिद्धौ कुरुनन्दन ||"),
CardInfo("Jnana Yoga","Yellow","4","Purification","13.10,13.11,12","Much to prepare, you have. Lose the ego, reflect on suffering in birth, disease, old age, and death. Cling not to the changing, nor possessions. Let go of desires, for happiness, it does not bring. Through equanimity, In joy and sorrow, purify the mind, for a brighter path it reveals.","असक्तिरनभिष्वङ्ग: पुत्रदारगृहादिषु | नित्यं च समचित्तत्वमिष्टानिष्टोपपत्तिषु || मयि चानन्ययोगेन भक्तिरव्यभिचारिणी | विविक्तदेशसेवित्वमरतिर्जनसंसदि || अध्यात्मज्ञाननित्यत्वं तत्वज्ञानार्थदर्शनम् | एतज्ज्ञानमिति प्रोक्तमज्ञानं यदतोऽन्यथा ||"),
CardInfo("Jnana Yoga","Yellow","5","Viveka","2.2","Consciousness, Self, the Atman pervades all that is changing in the world. Birth it has not, nor will it ever die. Created it was not, nor will it ever be created and what is not created is not destroyed. ","कुतस्त्वा कश्मलमिदं विषमे समुपस्थितम् | अनार्यजुष्टमस्वर्ग्यमकीर्तिकरमर्जुन ||"),
CardInfo("Jnana Yoga","Yellow","6","Vairagya","14.24","alike in joy and sorrow, the wise one is. Let go of the ego, Found the Self, they have. Rock, gold, or mud, all the same to them. Pleasure and pain, the same they feel.","समदु:खसुख: स्वस्थ: समलोष्टाश्मकाञ्चन: | तुल्यप्रियाप्रियो धीरस्तुल्यनिन्दात्मसंस्तुति: || मानापमानयोस्तुल्यस्तुल्यो मित्रारिपक्षयो: | सर्वारम्भपरित्यागी गुणातीत: स उच्यते ||"),
CardInfo("Jnana Yoga","Yellow","7","Go Deeper","18.63","Thus, I have explained to you this knowledge that is more secret than all secrets. Ponder over it deeply, and then do as you wish.","इति ते ज्ञानमाख्यातं गुह्याद्गुह्यतरं मया | विमृश्यैतदशेषेण यथेच्छसि तथा कुरु ||"),
CardInfo("Jnana Yoga","Yellow","8","Theory","13.5","Sung the truth, Great sages have, about the seen and the seer in manifold ways. Sound logic and concluisive evidence for the truth Vedic hymns state, and Brahma Sūtra reveals.","ऋषिभिर्बहुधा गीतं छन्दोभिर्विविधै: पृथक् | ब्रह्मसूत्रपदैश्चैव हेतुमद्भिर्विनिश्चितै: ||"),
CardInfo("Jnana Yoga","Yellow","9","wisdom","13.34,13.35","Like shines one Sun light on all planets its light. One soul shines light on the entire body-mind. See this difference, those who can, with wisdom's eyes: between the vehicle(body-mind) and the soul that drives it. They escape from material world to the ultimate destination.","यथा प्रकाशयत्येक: कृत्स्नं लोकमिमं रवि: | क्षेत्रं क्षेत्री तथा कृत्स्नं प्रकाशयति भारत || क्षेत्रक्षेत्रज्ञयोरेवमन्तरं ज्ञानचक्षुषा | भूतप्रकृतिमोक्षं च ये विदुर्यान्ति ते परम् ||"),
CardInfo("Jnana Yoga","Yellow","10","Enlightenment","4.24,3.17","Completely one with God-consciousness is such a one for whom: the offering is Brahman, the ladle with which it is offered is Brahman, the act of offering is Brahman, and the sacrificial fire is also Brahman. They understand the mystery of one appearing as infinitely many!","ब्रह्मार्पणं ब्रह्म हविर्ब्रह्माग्नौ ब्रह्मणा हुतम् | ब्रह्मैव तेन गन्तव्यं ब्रह्मकर्मसमाधिना || यस्त्वात्मरतिरेव स्यादात्मतृप्तश्च मानव: | आत्मन्येव च सन्तुष्टस्तस्य कार्यं न विद्यते ||"),
CardInfo("Jnana Yoga","Yellow","Av","Avatar","4.7","Whenever there is a decline in righteousness and an increase in unrighteousness O Arjun at that time I manifest Myself on earth. ","यदा यदा हि धर्मस्य ग्लानिर्भवति भारत | अभ्युत्थानमधर्मस्य तदात्मानं सृजाम्यहम् ||"),
CardInfo("Jnana Yoga","Yellow","T","Tamas","14.8","O Arjun tamo guána which is born of ignorance is the cause of illusion for the embodied souls. It deludes all living beings through negligence laziness and sleep. ","तमस्त्वज्ञानजं विद्धि मोहनं सर्वदेहिनाम् । प्रमादालस्यनिद्राभिस्तन्निबध्नाति भारत ||"),
CardInfo("Jnana Yoga","Yellow","R","Rajas","14.7","O Arjun, rajo guna is of the nature of passion. It arises from worldly desires and affections, and binds the soul through attachment to fruitive actions.","रजो रागात्मकं विद्धि तृष्णासङ्गसमुद्भवम् | तन्निबध्नाति कौन्तेय कर्मसङ्गेन देहिनम् ||"),
CardInfo("Jnana Yoga","Yellow","S","Sattva","14.6","Amongst these, sattva guna, the mode of goodness, being purer than the others, is illuminating and full of well-being. O sinless one, it binds the soul by creating attachment for a sense of happiness and knowledge.","तत्र सत्त्वं निर्मलत्वात्प्रकाशकमनामयम् | सुखसङ्गेन बध्नाति ज्ञानसङ्गेन चानघ ||"),
CardInfo("Jnana Yoga","Yellow","M","Maya","7.14","My divine energy Maya consisting of the three modes of nature is very difficult to overcome. But those who surrender unto Me cross over it easily. ","दैवी ह्येषा गुणमयी मम माया दुरत्यया | मामेव ये प्रपद्यन्ते मायामेतां तरन्ति ते ||"),
CardInfo("Jnana Yoga","Yellow","Sa","Samsara","9.3","People who have no faith in this dharma are unable to attain Me, O conqueror of enemies. They repeatedly come back to this world in the cycle of birth and death.","अश्रद्दधाना: पुरुषा धर्मस्यास्य परन्तप | अप्राप्य मां निवर्तन्ते मृत्युसंसारवर्त्मनि ||"),
CardInfo("Jnana Yoga","Yellow","Re","Rebirth","2.12","Never was there a time when I did not exist, nor you, nor all these kings; nor in the future shall any of us cease to be.","न त्वेवाहं जातु नासं न त्वं नेमे जनाधिपाः | न चैव न भविष्याम: सर्वे वयमत: परम् ||"),
CardInfo("Jnana Yoga","Yellow","So","Soul","2.24","The soul is unbreakable and incombustible; it can neither be dampened nor dried. It is everlasting, in all places, unalterable, immutable, and primordial.","अच्छेद्योऽयमदाह्योऽयमक्लेद्योऽशोष्य एव च | नित्य: सर्वगत: स्थाणुरचलोऽयं सनातन: ||"),
CardInfo("Bhakthi Yoga","Red","0","Doubting","16.8","Lost faith, some have. They say time and universe is a coincidence without a guiding God.","असत्यमप्रतिष्ठं ते जगदाहुरनीश्वरम् | अपरस्परसम्भूतं किमन्यत्कामहैतुकम् ||"),
CardInfo("Bhakthi Yoga","Red","1","Distress","1.29,1.31","Arjua said: My whole body shivers; hair stands on its end. My bow, the Gandiv, slips from my grasp, and my skin burns all over. My mind spins like a tornado; I am unable to hold myself steady. O Krishna, I only see doom.","वेपथुश्च शरीरे मे रोमहर्षश्च जायते || गाण्डीवं स्रंसते हस्तात्त्वक्चै व परिदह्यते | न च शक्नोम्यवस्थातुं भ्रमतीव च मे मन: || निमित्तानि च पश्यामि विपरीतानि केशव | न च श्रेयोऽनुपश्यामि हत्वा स्वजनमाहवे ||"),
CardInfo("Bhakthi Yoga","Red","2","Pull Towards God","7.16","O best amongst humans, four kinds of pious people engage in My devotion—the distressed, the seekers of knowledge, the seekers of worldly possessions, and those who are situated in knowledge.","चतुर्विधा भजन्ते मां जना: सुकृतिनोऽर्जुन | आर्तो जिज्ञासुरर्थार्थी ज्ञानी च भरतर्षभ ||"),
CardInfo("Bhakthi Yoga","Red","3","faith develops","11.41,11.42","Arjuna spoke: “O dear Friend Krishna” Ignorant of your Godly nature childishly treated you with disrespect, while playing, resting, sitting, eating, when alone, or before others—for all that I ask forgiveness.","सखेति मत्वा प्रसभं यदुक्तं हे कृष्ण हे यादव हे सखेति | अजानता महिमानं तवेदंमया प्रमादात्प्रणयेन वापि || यच्चावहासार्थमसत्कृतोऽसि विहारशय्यासनभोजनेषु | एकोऽथवाप्यच्युत तत्समक्षंतत्क्षामये त्वामहमप्रमेयम् ||"),
CardInfo("Bhakthi Yoga","Red","4","Practices","12.9,12.10,12.11","Try to fix your mind steadily on Me, O Arjun, if not remember Me while engaged in the world. If you fail to remember Me, then just work for Me. If you are unable work for Me, then just offer the fruits of your actions to Me. Doing work as service, you shall achieve the state of perfection.","अथ चित्तं समाधातुं न शक्नोषि मयि स्थिरम् | अभ्यासयोगेन ततो मामिच्छाप्तुं धनञ्जय || अभ्यासेऽप्यसमर्थोऽसि मत्कर्मपरमो भव | मदर्थमपि कर्माणि कुर्वन्सिद्धिमवाप्स्यसि || अथैतदप्यशक्तोऽसि कर्तुं मद्योगमाश्रित: | सर्वकर्मफलत्यागं तत: कुरु यतात्मवान् ||"),
CardInfo("Bhakthi Yoga","Red","5","Love","9.26","In the depths of your loving heart, even the simplest offering - a leaf, a flower, a fruit, or water - becomes the most precious gift to the Divine. ","पत्रं पुष्पं फलं तोयं यो मे भक्त्या प्रयच्छति | तदहं भक्त्युपहृतमश्नामि प्रयतात्मन: ||"),
CardInfo("Bhakthi Yoga","Red","6","God","9.4,9.5,9.6","I am in all beings but wait, all beings are in Me, I am not in them and yet no being is in Me. Behold the paradox of My divine energy! Although I am the Creator and Sustainer of all living beings, I am not influenced by them like the mighty wind blowing everywhere has no effect on space. ","मया ततमिदं सर्वं जगदव्यक्तमूर्तिना | मत्स्थानि सर्वभूतानि न चाहं तेष्ववस्थित: || न च मत्स्थानि भूतानि पश्य मे योगमैश्वरम् | भूतभृन्न च भूतस्थो ममात्मा भूतभावन: || यथाकाशस्थितो नित्यं वायु: सर्वत्रगो महान् | तथा सर्वाणि भूतानि मत्स्थानीत्युपधारय ||"),
CardInfo("Bhakthi Yoga","Red","7","Devotion","12.2","Those who fix their minds on Me and always engage in My devotion with steadfast faith, I consider them to be the best devotees and uplift them to my eternal abode.","मय्यावेश्य मनो ये मां नित्ययुक्ता उपासते | श्रद्धया परयोपेतास्ते मे युक्ततमा मता: ||"),
CardInfo("Bhakthi Yoga","Red","8","Grace of God","12.7","Those who, with steadfast devotion, ever meditate on My auspicious form,to them I carry what they lack and preserve what they have, nurturing them towards liberation.","ये तु सर्वाणि कर्माणि मयि संन्न्यस्य मत्पर: | अनन्येनैव योगेन मां ध्यायन्त उपासते || तेषामहं समुद्धर्ता मृत्युसंसारसागरात् | भवामि नचिरात्पार्थ मय्यावेशितचेतसाम् ||"),
CardInfo("Bhakthi Yoga","Red","9","Glory of God","10.25","I am 'Om' amongst sounds. repetition of Holy Name amongst chants; amongst immovable things I am the Himalayas, among secrets I am silence, amongst all that controls I am the endless time. What I declared is a mere sample of My infinite glories.","महर्षीणां भृगुरहं गिरामस्म्येकमक्षरम् | यज्ञानां जपयज्ञोऽस्मि स्थावराणां हिमालय: ||"),
CardInfo("Bhakthi Yoga","Red","10","Attain God","8.15,8.28","Having understood the inherent connection with God, they gain merit far beyond the fruits of rituals, knowledge, sacrifices, and charities. Like lotus flowers blooming pristine above the muck, they rise above all suffering, finding eternal sanctuary and boundless love in the embrace of God.","शरीरवाङ्मनोभिर्यत्कर्म प्रारभते नर: | न्याय्यं वा विपरीतं वा पञ्चैते तस्य हेतव: || अयुक्त: प्राकृत: स्तब्ध: शठो नैष्कृतिकोऽलस: | विषादी दीर्घसूत्री च कर्ता तामस उच्यते ||"),
CardInfo("Bhakthi Yoga","Red","0","Doubting","7.15","Four kinds of people do not have faith in me—those ignorant of knowledge, those who lazily follow their lower nature though capable of knowing Me, those with deluded intellect, and those with a demoniac nature.","न मां दुष्कृतिनो मूढा: प्रपद्यन्ते नराधमा: | माययापहृतज्ञाना आसुरं भावमाश्रिता: ||"),
CardInfo("Bhakthi Yoga","Red","1","Distress","7.21,7.22,7.23","Whatever belief one desires other than me, I strengthen that very faith. Fueled by faith, many desires are fulfilled. It is I who arrange these rewards. But know that these gains are temporary, and suffering follows soon. In Contrast, true devotees seek only me and find eternal blessings.","यो यो यां यां तनुं भक्त: श्रद्धयार्चितुमिच्छति | तस्य तस्याचलां श्रद्धां तामेव विदधाम्यहम् || स तया श्रद्धया युक्तस्तस्याराधनमीहते | लभते च तत: कामान्मयैव विहितान्हि तान् || अन्तवत्तु फलं तेषां तद्भवत्यल्पमेधसाम् | देवान्देवयजो यान्ति मद्भक्ता यान्ति मामपि ||"),
CardInfo("Bhakthi Yoga","Red","2","Pull Towards God","6.44","Some are drawn towards God, even against their will, on the strength of their past discipline. Rise above rituals and catch faith, such seekers natually do.","पूर्वाभ्यासेन तेनैव ह्रियते ह्यवशोऽपि स: | जिज्ञासुरपि योगस्य शब्दब्रह्मातिवर्तते ||"),
CardInfo("Bhakthi Yoga","Red","3","faith develops","18.78","Wherever there is Shree Krishna, the Lord of all Yog, there will also certainly be unending opulence, victory, prosperity, and righteousness. Of this, I am certain.","यत्र योगेश्वर: कृष्णो यत्र पार्थो धनुर्धर: | तत्र श्रीर्विजयो भूतिध्रुवा नीतिर्मतिर्मम ||"),
CardInfo("Bhakthi Yoga","Red","4","Practices","12.13,12.14","With compassion for all beings, extinguish the fires of anger and pride. Through steady practice, cultivate devotion, finding solace in our divine connection. The Supreme Being cherishes those who embody these virtues. Surrender your mind and heart to Him, for God's grace then one finds.","अद्वेष्टा सर्वभूतानां मैत्र: करुण एव च | निर्ममो निरहङ्कार: समदु:खसुख: क्षमी || सन्तुष्ट: सततं योगी यतात्मा दृढनिश्चय: | मय्यर्पितमनोबुद्धिर्यो मद्भक्त: स मे प्रिय: ||"),
CardInfo("Bhakthi Yoga","Red","5","Love","4.11","In whatever way people surrender unto Me, I reciprocate accordingly. Everyone follows My path, knowingly or unknowingly. Having known this, surrender whole heartedly and bathe in ocean of grace.","ये यथा मां प्रपद्यन्ते तांस्तथैव भजाम्यहम् | मम वर्त्मानुवर्तन्ते मनुष्या: पार्थ सर्वश: ||"),
CardInfo("Bhakthi Yoga","Red","6","God","9.18","I am the Supreme Goal of all living beings, and I am also their Sustainer, Master, Witness, Abode, Shelter, and Friend. I am the Origin, End, and Resting Place of creation; I am the Repository and Eternal Seed.","गतिर्भर्ता प्रभु: साक्षी निवास: शरणं सुहृत् | प्रभव: प्रलय: स्थानं निधानं बीजमव्ययम् ||"),
CardInfo("Bhakthi Yoga","Red","7","Devotion","9.14","Always singing My divine glories, striving with great determination, and humbly bowing down before Me, constantly worship Me in loving devotion. Such devotees get rid of all bad habbits, transcend all suffering and enjoy unending wellspring of devotion.","सततं कीर्तयन्तो मां यतन्तश्च दृढव्रता: | नमस्यन्तश्च मां भक्त्या नित्ययुक्ता उपासते ||"),
CardInfo("Bhakthi Yoga","Red","8","Grace of God","10.11"," Out of compassion for the faithful, I, dwelling in their hearts, destroy with the shining lamp of knowledge the darkness born of ignorance after which one transcends suffering in all situations.","तेषामेवानुकम्पार्थमहमज्ञानजं तम: | नाशयाम्यात्मभावस्थो ज्ञानदीपेन भास्वता ||"),
CardInfo("Bhakthi Yoga","Red","9","Glory of God","10.41","Whatever you see as beautiful, glorious, or powerful, know it to spring from but a spark of My splendor. I am the beginning, middle, and end of all beings. Simply know that by one fraction of My being, I pervade and support this entire creation.","यद्यद्विभूतिमत्सत्त्वं श्रीमदूर्जितमेव वा | तत्देवावगच्छ त्वं मम तेजोंऽशसम्भवम् ||"),
CardInfo("Bhakthi Yoga","Red","10","Attain God","11.10,11.11,11.12","To such bhakthas, God reveals His divine form, blazing brighter than a thousand suns. With fragrance of heavens, this powerful form with countless eyes and hands stands beyond all comprehension, theirs to behold – an experience that fills them with everlasting awe.","अनेकवक्त्रनयनमनेकाद्भुतदर्शनम् | अनेकदिव्याभरणं दिव्यानेकोद्यतायुधम् || दिव्यमाल्याम्बरधरं दिव्यगन्धानुलेपनम् | सर्वाश्चर्यमयं देवमनन्तं विश्वतोमुखम् || दिवि सूर्यसहस्रस्य भवेद्युगपदुत्थिता | यदि भा: सदृशी सा स्याद्भासस्तस्य महात्मन: ||"),
CardInfo("Bhakthi Yoga","Red","Av","Avatar","4.7","Whenever there is a decline in righteousness and an increase in unrighteousness O Arjun at that time I manifest Myself on earth. ","यदा यदा हि धर्मस्य ग्लानिर्भवति भारत | अभ्युत्थानमधर्मस्य तदात्मानं सृजाम्यहम् ||"),
CardInfo("Bhakthi Yoga","Red","T","Tamas","14.8","O Arjun tamo guána which is born of ignorance is the cause of illusion for the embodied souls. It deludes all living beings through negligence laziness and sleep. ","तमस्त्वज्ञानजं विद्धि मोहनं सर्वदेहिनाम् | प्रमादालस्यनिद्राभिस्तन्निबध्नाति भारत ||"),
CardInfo("Bhakthi Yoga","Red","R","Rajas","14.7","O Arjun, rajo guna is of the nature of passion. It arises from worldly desires and affections, and binds the soul through attachment to fruitive actions.","रजो रागात्मकं विद्धि तृष्णासङ्गसमुद्भवम् | तन्निबध्नाति कौन्तेय कर्मसङ्गेन देहिनम् ||"),
CardInfo("Bhakthi Yoga","Red","S","Sattva","14.6","Amongst these, sattva guna, the mode of goodness, being purer than the others, is illuminating and full of well-being. O sinless one, it binds the soul by creating attachment for a sense of happiness and knowledge.","तत्र सत्त्वं निर्मलत्वात्प्रकाशकमनामयम् | सुखसङ्गेन बध्नाति ज्ञानसङ्गेन चानघ ||"),
CardInfo("Bhakthi Yoga","Red","M","Maya","7.14","My divine energy Maya consisting of the three modes of nature is very difficult to overcome. But those who surrender unto Me cross over it easily. ","दैवी ह्येषा गुणमयी मम माया दुरत्यया | मामेव ये प्रपद्यन्ते मायामेतां तरन्ति ते ||"),
CardInfo("Bhakthi Yoga","Red","Sa","Samsara","9.3","People who have no faith in this dharma are unable to attain Me, O conqueror of enemies. They repeatedly come back to this world in the cycle of birth and death.","अश्रद्दधाना: पुरुषा धर्मस्यास्य परन्तप | अप्राप्य मां निवर्तन्ते मृत्युसंसारवर्त्मनि ||"),
CardInfo("Bhakthi Yoga","Red","Re","Rebirth","2.12","Never was there a time when I did not exist, nor you, nor all these kings; nor in the future shall any of us cease to be.","न त्वेवाहं जातु नासं न त्वं नेमे जनाधिपाः | न चैव न भविष्याम: सर्वे वयमत: परम् ||"),
CardInfo("Bhakthi Yoga","Red","So","Soul","2.24","The soul is unbreakable and incombustible; it can neither be dampened nor dried. It is everlasting, in all places, unalterable, immutable, and primordial.","अच्छेद्योऽयमदाह्योऽयमक्लेद्योऽशोष्य एव च | नित्य: सर्वगत: स्थाणुरचलोऽयं सनातन: ||"),
CardInfo("Karma Yoga","Green","0","Bondage","18.27,18.28","Trapped in Maya, the passionate act with fear, stress and anxiety. Others, cloaked by laziness, loose interest. Both, blind to the consequences of their choices, inflict pain on the world. They are like children playing in the sand, unaware of the tide that will wash away all.","रागी कर्मफलप्रेप्सुर्लुब्धो हिंसात्मकोऽशुचि: | हर्षशोकान्वित: कर्ता राजस: परिकीर्तित: || अयुक्त: प्राकृत: स्तब्ध: शठो नैष्कृतिकोऽलस: | विषादी दीर्घसूत्री च कर्ता तामस उच्यते ||"),
CardInfo("Karma Yoga","Green","1","Grief","3.36","Arjuna asked: Why do people commit sin, become lazy, and fearful even against their own wish, as if driven by an unseen force within?","अथ केन प्रयुक्तोऽयं पापं चरति पूरुष: | अनिच्छन्नपि वार्ष्णेय बलादिव नियोजित: ||"),
CardInfo("Karma Yoga","Green","2","Motivation","2.1,2.3","Seeing Arjuna in tears, full of pity and grief, Krishna spoke with a smile. Why has this doubt gripped you at this important hour? This isn't the way for a hero. It won't bring glory, only shame. Don't give in to this weakness. Be strong, rise above it, O, conqueror of evil!","तं तथा कृपयाविष्टमश्रुपूर्णाकुलेक्षणम् | विषीदन्तमिदं वाक्यमुवाच मधुसूदन: ||"),
CardInfo("Karma Yoga","Green","3","Purpose","2.32,18.46","happy are the people who find a purpose in their profession opening for them the stairway to heaven. By performing one’s natural occupation well, one worships work itself and benefits all living beings. By such performance of work, a person easily attains perfection.","यदृच्छया चोपपन्नं स्वर्गद्वारमपावृतम् | सुखिन: क्षत्रिया: पार्थ लभन्ते युद्धमीदृशम् || यत: प्रवृत्तिर्भूतानां येन सर्वमिदं ततम् | स्वकर्मणा तमभ्यर्च्य सिद्धिं विन्दति मानव: ||"),
CardInfo("Karma Yoga","Green","4","Self-Control","2.6","The senses are very strong and can pull even the mind of a person with self-control into bad habbits. ","न चैतद्विद्म: कतरन्नो गरीयोयद्वा जयेम यदि वा नो जयेयु: | यानेव हत्वा न जिजीविषामस्तेऽवस्थिता: प्रमुखे धार्तराष्ट्रा: ||"),
CardInfo("Karma Yoga","Green","5","Training","16.1,16.2,16.3","Purify and focus the mind to prepare for freedom through fearlessness, noble thoughts, learning, generosity, sense-control, sacrifice, simple life, honesty, non-violence, truthfullness, calm, peace, detachment, and avoid fault finding.","अभयं सत्त्वसंशुद्धिर्ज्ञानयोगव्यवस्थिति: | दानं दमश्च यज्ञश्च स्वाध्यायस्तप आर्जवम् || अहिंसा सत्यमक्रोधस्त्याग: शान्तिरपैशुनम् | दया भूतेष्वलोलुप्त्वं मार्दवं ह्रीरचापलम् || तेज: क्षमा धृति: शौचमद्रोहोनातिमानिता | भवन्ति सम्पदं दैवीमभिजातस्य भारत ||"),
CardInfo("Karma Yoga","Green","6","Action-Inaction","4.16,4.19","Action is superior to inaction as even staying alive requires effort. But what is action and inaction? Hear this secret: Those who see action in inaction and inaction in action are truly wise. Work done without desire, and without worrying about outcome, is action. All else is inaction.","किं कर्म किमकर्मेति कवयोऽप्यत्र मोहिता: | तत्ते कर्म प्रवक्ष्यामि यज्ज्ञात्वा मोक्ष्यसेऽशुभात् || यस्य सर्वे समारम्भा: कामसङ्कल्पवर्जिता: | ज्ञानाग्निदग्धकर्माणं तमाहु: पण्डितं बुधा: ||"),
CardInfo("Karma Yoga","Green","7","Leadership","3.20,3.21","Action is superior to inaction as even staying alive requires effort. But what is action and inaction? Hear this secret: Those who see action in inaction and inaction in action are truly wise. Work done without desire, and without worrying about outcome, is action. All else is inaction.","कर्मणैव हि संसिद्धिमास्थिता जनकादय: | लोकसंग्रहमेवापि सम्पश्यन्कर्तुमर्हसि || यद्यदाचरति श्रेष्ठस्तत्तदेवेतरो जन: | स यत्प्रमाणं कुरुते लोकस्तदनुवर्तते ||"),
CardInfo("Karma Yoga","Green","8","Work Instruments","13.3","They alone are wise who understand that all actions are performed by material nature using body as the instrument while the embodied soul actually does nothing. ","क्षेत्रज्ञं चापि मां विद्धि सर्वक्षेत्रेषु भारत | क्षेत्रक्षेत्रज्ञयोर्ज्ञानं यत्तज्ज्ञानं मतं मम ||"),
CardInfo("Karma Yoga","Green","9","KarmaYoga","2.39,2.40","Now listen, O Parth, as I reveal Buddhi Yog, or the Yog of Intellect. When you work with such understanding, you will be freed from the bondage of karma. Working in this state of consciousness, there is no loss or adverse result, and even a little effort saves one from great danger.","एषा तेऽभिहिता साङ्ख्येबुद्धिर्योगे त्विमां शृणु | बुद्ध्या युक्तो यया पार्थकर्मबन्धं प्रहास्यसि || नेहाभिक्रमनाशोऽस्ति प्रत्यवायो न विद्यते | स्वल्पमप्यस्य धर्मस्य त्रायते महतो भयात् ||"),
CardInfo("Karma Yoga","Green","10","Freedom","2.51","The wise endowed with equanimity of intellect, abandon attachment to the fruits of actions, which bind one to the cycle of life and death. By working in such consciousness, they attain the state beyond all suffering.","कर्मजं बुद्धियुक्ता हि फलं त्यक्त्वा मनीषिण: | जन्मबन्धविनिर्मुक्ता: पदं गच्छन्त्यनामयम् ||"),
CardInfo("Karma Yoga","Green","0","Bondage","16.23","Leaving aside dharma, those who act under the impulse of selfish desire or fail to act in their duty, attain neither perfection, nor happiness, nor the supreme goal in life.","य: शास्त्रविधिमुत्सृज्य वर्तते कामकारत: | न स सिद्धिमवाप्नोति न सुखं न परां गतिम् ||"),
CardInfo("Karma Yoga","Green","1","Grief","1.47","Arjuna declared, I don't want victory, a kingdom, or any happiness that comes with them. I refuse to fight! Overwhelmed with grief and distress, Arjuna dropped his bow and arrows, slumping down in his chariot seat.","एवमुक्त्वार्जुन: सङ्ख्ये रथोपस्थ उपाविशत् | विसृज्य सशरं चापं शोकसंविग्नमानस: ||"),
CardInfo("Karma Yoga","Green","2","Motivation","2.14","Contact between the senses and their objects generate perceptions of hot, cold, pain and pleasure. These are non-permanent, and come and go like the winter and summer seasons. O descendent, One must learn to tolerate them without being disturbed.","मात्रास्पर्शास्तु कौन्तेय शीतोष्णसुखदु: खदा: | आगमापायिनोऽनित्यास्तांस्तितिक्षस्व भारत ||"),
CardInfo("Karma Yoga","Green","3","Purpose","18.47","It's better to do your own job well, even if you're not perfect at it, than to do someone else's job. When you focus on what you're naturally suited for, you avoid any wrongdoing and a sense of fulfillment.","श्रेयान्स्वधर्मो विगुण: परधर्मात्स्वनुष्ठितात् | स्वभावनियतं कर्म कुर्वन्नाप्नोति किल्बिषम् ||"),
CardInfo("Karma Yoga","Green","4","Self-Control","6.35, 3.43","The mind is very difficult to restrain. But by practice and detachment, it can be controlled. Knowing the soul to be superior, subdue the senses, mind, and intellect and re-gain control over yourself.","संशयं महाबाहो मनो दुर्निग्रहं चलम् | अभ्यासेन तु कौन्तेय वैराग्येण च गृह्यते || एवं बुद्धे: परं बुद्ध्वा संस्तभ्यात्मानमात्मना | जहि शत्रुं महाबाहो कामरूपं दुरासदम् ||"),
CardInfo("Karma Yoga","Green","5","Training","3.43","These divine virtues are practices to attain freedom by cleansing the mind: compassion towards all, absence of greed, gentleness, modesty, and lack of fickleness; vigor, forgiveness, strength, cleanliness, non-enmity, and absence of pride.","एवं बुद्धे: परं बुद्ध्वा संस्तभ्यात्मानमात्मना | जहि शत्रुं महाबाहो कामरूपं दुरासदम् ||"),
CardInfo("Karma Yoga","Green","6","Action-Inaction","4.18","Action is superior to inaction. By ceasing activity, even your bodily maintenance will not be possible.Although performing all kinds of actions they never get entangled and remain ever free.","कर्मण्यकर्म य: पश्येदकर्मणि च कर्म य: | स बुद्धिमान्मनुष्येषु स युक्त: कृत्स्नकर्मकृत् ||"),
CardInfo("Karma Yoga","Green","7","Leadership","3.22-23","There is no duty for Me to do in all the three worlds O Parth nor do I have anything to gain or attain. Yet I am engaged in prescribed duties. For if I did not carefully perform the prescribed duties O Parth all men would follow My path in all respects. ","ुरुष: प्रकृतिस्थो हि भुङक्ते प्रकृतिजान्गुणान् | कारणं गुणसङ्गोऽस्य सदसद्योनिजन्मसु || उपद्रष्टानुमन्ता च भर्ता भोक्ता महेश्वर: | परमात्मेति चाप्युक्तो देहेऽस्मिन्पुरुष: पर: ||"),
CardInfo("Karma Yoga","Green","8","Work Instruments","11.32-33","The Supreme Lord said: I am mighty Time and the work is already done. Body is the expert instrument. Therefore arise, awake, do your duty and attain honor! ","कालोऽस्मि लोकक्षयकृत्प्रवृद्धोलोकान्स माहर्तुमिह प्रवृत्त: | ऋतेऽपि त्वां न भविष्यन्ति सर्वेयेऽवस्थिता: प्रत्यनीकेषु योधा: || तस्मात्त्वमुत्तिष्ठ यशो लभस्वजित्वा शत्रून्भुङ् क्ष्व राज्यं समृद्धम् | मयैवैते निहता: पूर्वमेवनिमित्तमात्रं भव सव्यसाचिन् ||"),
CardInfo("Karma Yoga","Green","9","KarmaYoga","2.47","You have a right to perform your prescribed duties, but you are not entitled to the fruits of your actions. Never consider yourself to be the cause of the results of your activities, nor be attached to inaction.","कर्मण्येवाधिकारस्ते मा फलेषु कदाचन | मा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि ||"),
CardInfo("Karma Yoga","Green","10","Freedom","3.31","Those who abide by these teachings of Mine with profound faith and free from envy are released from the bondage of karma. ","ये मे मतमिदं नित्यमनुतिष्ठन्ति मानवा: | श्रद्धावन्तोऽनसूयन्तो मुच्यन्ते तेऽपि कर्मभि: ||"),
CardInfo("Karma Yoga","Green","Av","Avatar","4.7","Whenever there is a decline in righteousness and an increase in unrighteousness O Arjun at that time I manifest Myself on earth. ","यदा यदा हि धर्मस्य ग्लानिर्भवति भारत | अभ्युत्थानमधर्मस्य तदात्मानं सृजाम्यहम् ||"),
CardInfo("Karma Yoga","Green","T","Tamas","14.8","O Arjun tamo guána which is born of ignorance is the cause of illusion for the embodied souls. It deludes all living beings through negligence laziness and sleep. ","तमस्त्वज्ञानजं विद्धि मोहनं सर्वदेहिनाम् | प्रमादालस्यनिद्राभिस्तन्निबध्नाति भारत ||"),
CardInfo("Karma Yoga","Green","R","Rajas","14.7","O Arjun, rajo guna is of the nature of passion. It arises from worldly desires and affections, and binds the soul through attachment to fruitive actions.","रजो रागात्मकं विद्धि तृष्णासङ्गसमुद्भवम् | तन्निबध्नाति कौन्तेय कर्मसङ्गेन देहिनम् ||"),
CardInfo("Karma Yoga","Green","S","Sattva","14.6","Amongst these, sattva guna, the mode of goodness, being purer than the others, is illuminating and full of well-being. O sinless one, it binds the soul by creating attachment for a sense of happiness and knowledge.","तत्र सत्त्वं निर्मलत्वात्प्रकाशकमनामयम् | सुखसङ्गेन बध्नाति ज्ञानसङ्गेन चानघ ||"),
CardInfo("Karma Yoga","Green","M","Maya","7.14","My divine energy Maya consisting of the three modes of nature is very difficult to overcome. But those who surrender unto Me cross over it easily. ","दैवी ह्येषा गुणमयी मम माया दुरत्यया | मामेव ये प्रपद्यन्ते मायामेतां तरन्ति ते ||"),
CardInfo("Karma Yoga","Green","Sa","Samsara","9.3","People who have no faith in this dharma are unable to attain Me, O conqueror of enemies. They repeatedly come back to this world in the cycle of birth and death.","अश्रद्दधाना: पुरुषा धर्मस्यास्य परन्तप | अप्राप्य मां निवर्तन्ते मृत्युसंसारवर्त्मनि ||"),
CardInfo("Karma Yoga","Green","Re","Rebirth","2.12","Never was there a time when I did not exist, nor you, nor all these kings; nor in the future shall any of us cease to be.","न त्वेवाहं जातु नासं न त्वं नेमे जनाधिपाः | न चैव न भविष्याम: सर्वे वयमत: परम् ||"),
CardInfo("Karma Yoga","Green","So","Soul","2.24","The soul is unbreakable and incombustible; it can neither be dampened nor dried. It is everlasting, in all places, unalterable, immutable, and primordial.","अच्छेद्योऽयमदाह्योऽयमक्लेद्योऽशोष्य एव च | नित्य: सर्वगत: स्थाणुरचलोऽयं सनातन: ||"),
CardInfo("Raja Yoga","Blue","0","Restless Mind","6.34","The mind is very restless turbulent strong and obstinate O Krishna. It appears to me that it is more difficult to control than the wind. ","चञ्चलं हि मन: कृष्ण प्रमाथि बलवद्दृढम् | तस्याहं निग्रहं मन्ये वायोरिव सुदुष्करम् ||"),
CardInfo("Raja Yoga","Blue","1","Unhealthy","2.66","But an undisciplined person who has not controlled the mind and senses can neither have a resolute intellect nor steady contemplation on God. For one who never unites the mind with God there is no peace; and how can one who lacks peace be happy? ","नास्ति बुद्धिरयुक्तस्य न चायुक्तस्य भावना | न चाभावयत: शान्तिरशान्तस्य कुत: सुखम् ||"),
CardInfo("Raja Yoga","Blue","2","Healing","6.5","Elevate yourself through the power of your mind and not degrade yourself for the mind can be the friend and also the enemy of the self. ","उद्धरेदात्मनात्मानं नात्मानमवसादयेत् | आत्मैव ह्यात्मनो बन्धुरात्मैव रिपुरात्मन: ||"),
CardInfo("Raja Yoga","Blue","3","Yama","10.4,10.5","From Me alone arise the varieties of qualities in humans, such as intellect, knowledge, clarity of thought, forgiveness, truthfulness, control over the senses and mind, joy and sorrow, birth and death, fear and courage, non-violence, equanimity, contentment, austerity, charity, fame, and infamy.","बुद्धिर्ज्ञानमसम्मोह: क्षमा सत्यं दम: शम: | सुखं दु:खं भवोऽभावो भयं चाभयमेव च || अहिंसा समता तुष्टिस्तपो दानं यशोऽयश: | भवन्ति भावा भूतानां मत्त एव पृथग्विधा: ||"),
CardInfo("Raja Yoga","Blue","4","Niyama","17.8,17.9","Prefer juicy succulent foods that promote life span, virtue, strength, health, happiness and satisfaction. Avoid foods that are too bitter, too sour, salty, very hot, pungent, dry, and full of chillies that produce pain, grief, and disease.","आयु:सत्त्वबलारोग्यसुखप्रीतिविवर्धना: | रस्या: स्निग्धा: स्थिरा हृद्या आहारा: सात्त्विकप्रिया: || कट्वम्ललवणात्युष्णतीक्ष्णरूक्षविदाहिन: | आहारा राजसस्येष्टा दु:खशोकामयप्रदा: ||"),
CardInfo("Raja Yoga","Blue","5","Asana","6.13","He must hold the body neck and head firmly in a straight line and gaze at the tip of the nose without allowing the eyes to wander. ","तत्रैकाग्रं मन: कृत्वा यतचित्तेन्द्रियक्रिय: | उपविश्यासने युञ्ज्याद्योगमात्मविशुद्धये || समं कायशिरोग्रीवं धारयन्नचलं स्थिर: | सम्प्रेक्ष्य नासिकाग्रं स्वं दिशश्चानवलोकयन् ||"),
CardInfo("Raja Yoga","Blue","6","Pranayama","4.29,4.30","Some restrain incoming and outgoing breaths while purely absorbed in the regulation of the life-energy. Some curtail their food intake and offer the breath into the life-energy as sacrifice. All these knowers of sacrifice are cleansed of their impurities as a result of such performances. ","अपाने जुह्वति प्राणं प्राणेऽपानं तथापरे | प्राणापानगती रुद्ध्वा प्राणायामपरायणा: || अपरे नियताहारा: प्राणान्प्राणेषु जुह्वति | सर्वेऽप्येते यज्ञविदो यज्ञक्षपितकल्मषा: ||"),
CardInfo("Raja Yoga","Blue","7","Pratyahara","6.18","With thorough discipline, they learn to withdraw the mind from selfish cravings and rivet it on the unsurpassable good of the self. Such persons are said to be in Yog, and are free from all yearning of the senses.","यदा विनियतं चित्तमात्मन्येवावतिष्ठते | नि:स्पृह: सर्वकामेभ्यो युक्त इत्युच्यते तदा ||"),
CardInfo("Raja Yoga","Blue","8","YogaMat","6.11","To practice Yog, one should make an asan (seat) in a sanctified place, by placing Kuśh grass, deer skin, and a cloth, one over the other. The asan should be neither too high nor too low.","शुचौ देशे प्रतिष्ठाप्य स्थिरमासनमात्मन: | नात्युच्छ्रितं नातिनीचं चैलाजिनकुशोत्तरम् ||"),
CardInfo("Raja Yoga","Blue","9","Dhyana","6.19","Just as a lamp in a windless place does not flicker, so the disciplined mind of a yogi remains steady in meditation on the Supreme.","यथा दीपो निवातस्थो नेङ्गते सोपमा स्मृता | योगिनो यतचित्तस्य युञ्जतो योगमात्मन: ||"),
CardInfo("Raja Yoga","Blue","10","Samadhi","6.21,6.22","In that joyous state of Yog one experiences supreme boundless divine bliss. Having gained that state, one does not consider any other attainment to be greater. One is then not shaken even in the midst of the greatest calamity.","सुखमात्यन्तिकं यत्तद्बुद्धिग्राह्यमतीन्द्रियम् | वेत्ति यत्र न चैवायं स्थितश्चलति तत्त्वत: || यं लब्ध्वा चापरं लाभं मन्यते नाधिकं तत: | यस्मिन्स्थितो न दु:खेन गुरुणापि विचाल्यते ||"),
CardInfo("Raja Yoga","Blue","0","Restless Mind","16.11","They are obsessed with endless anxieties that end only with death. Still, they maintain with complete assurance that gratification of desires and accumulation of wealth is the highest purpose of life.","चिन्तामपरिमेयां च प्रलयान्तामुपाश्रिता: | कामोपभोगपरमा एतावदिति निश्चिता: ||"),
CardInfo("Raja Yoga","Blue","1","Unhealthy","18.8","To give up exercise because they are troublesome or cause bodily discomfort is renunciation in the mode of passion. Such renunciation is never beneficial or elevating. ","दु:खमित्येव यत्कर्म कायक्लेशभयात्यजेत् | स कृत्वा राजसं त्यागं नैव त्यागफलं लभेत् ||"),
CardInfo("Raja Yoga","Blue","2","Healing","6.7","The yogis who have conquered the mind rise above the dualities of cold and heat joy and sorrow and honor and dishonor. Such yogis remain peaceful and steadfast in their path to samadhi","जितात्मन: प्रशान्तस्य परमात्मा समाहित: | शीतोष्णसुखदु:खेषु तथा मानापमानयो: ||"),
CardInfo("Raja Yoga","Blue","3","Yama","6.9","The yogis look upon all—well-wishers, friends, foes, the pious, and the sinners—with an impartial intellect. The yogi who is of equal intellect toward friend, companion, and foe, neutral among enemies and relatives, and unbiased between the righteous and sinful, is considered to be distinguished among humans.","सुहृन्मित्रार्युदासीनमध्यस्थद्वेष्यबन्धुषु | साधुष्वपि च पापेषु समबुद्धिर्विशिष्यते ||"),
CardInfo("Raja Yoga","Blue","4","Niyama","6.16,6.17","O Arjun those who eat too much or too little sleep too much or too little cannot attain success in Yog. But those who are temperate in eating and recreation balanced in work and regulated in sleep can mitigate all sorrows by practicing Yog. ","अनेकचित्तविभ्रान्ता मोहजालसमावृता: | प्रसक्ता: कामभोगेषु पतन्ति नरकेऽशुचौ || आत्मसम्भाविता: स्तब्धा धनमानमदान्विता: | यजन्ते नामयज्ञैस्ते दम्भेनाविधिपूर्वकम् ||"),
CardInfo("Raja Yoga","Blue","5","Asana","8.12","Restraining all the gates of the body and fixing the mind in the heart region and then drawing the life-breath to the head one should get established in steadfast yogic concentration. ","सर्वद्वाराणि संयम्य मनो हृदि निरुध्य च | मूर्ध्न्याधायात्मन: प्राणमास्थितो योगधारणाम् ||"),
CardInfo("Raja Yoga","Blue","6","Pranayama","5.27,5.28","Shutting out all thoughts of external enjoyment with the gaze fixed on the space between the eye-brows equalizing the flow of the incoming and outgoing breath in the nostrils and thus controlling the senses mind and intellect the sage who becomes free from desire and fear ","स्पर्शान्कृत्वा बहिर्बाह्यांश्चक्षुश्चैवान्तरे भ्रुवो: | प्राणापानौ समौ कृत्वा नासाभ्यन्तरचारिणौ || यतेन्द्रियमनोबुद्धिर्मुनिर्मोक्षपरायण: | विगतेच्छाभयक्रोधो य: सदा मुक्त एव स: ||"),
CardInfo("Raja Yoga","Blue","7","Dharana","6.26","Whenever and wherever the restless and unsteady mind wanders, one should bring it back and continually focus it on God.","यतो यतो निश्चरति मनश्चञ्चलमस्थिरम् | ततस्ततो नियम्यैतदात्मन्येव वशं नयेत् ||"),
CardInfo("Raja Yoga","Blue","8","YogaMat","6.10","Those who seek Samadhi should reside in Yoga room, engaged in meditation with a controlled mind and body, getting rid of desires and possessions for enjoyment.","काममाश्रित्य दुष्पूरं दम्भमानमदान्विता: | मोहाद्गृहीत्वासद्ग्राहान्प्रवर्तन्तेऽशुचिव्रता: ||"),
CardInfo("Raja Yoga","Blue","9","Dhyana","6.1","Those who seek the state of Yog should reside in seclusion, constantly engaged in meditation with a controlled mind and body, getting rid of desires and possessions for enjoyment.","अनाश्रित: कर्मफलं कार्यं कर्म करोति य: | स संन्यासी च योगी च न निरग्निर्न चाक्रिय: ||"),
CardInfo("Raja Yoga","Blue","10","Samadhi","6.15,6.20","When the mind becomes still by the practice of Yog, then the yogi is able to behold the soul through the purified mind, and he rejoices in the inner joy. Thus, constantly keeping the mind absorbed in Me, the yogi of disciplined mind attains nirvan, and abides in Me in supreme peace.","ुञ्जन्नेवं सदात्मानं योगी नियतमानस: | शान्तिं निर्वाणपरमां मत्संस्थामधिगच्छति || यत्रोपरमते चित्तं निरुद्धं योगसेवया | यत्र चैवात्मनात्मानं पश्यन्नात्मनि तुष्यति ||"),
CardInfo("Raja Yoga","Blue","Av","Avatar","4.7","Whenever there is a decline in righteousness and an increase in unrighteousness O Arjun at that time I manifest Myself on earth. ","यदा यदा हि धर्मस्य ग्लानिर्भवति भारत | अभ्युत्थानमधर्मस्य तदात्मानं सृजाम्यहम् ||"),
CardInfo("Raja Yoga","Blue","T","Tamas","14.8","O Arjun tamo guána which is born of ignorance is the cause of illusion for the embodied souls. It deludes all living beings through negligence laziness and sleep. ","तमस्त्वज्ञानजं विद्धि मोहनं सर्वदेहिनाम् | प्रमादालस्यनिद्राभिस्तन्निबध्नाति भारत ||"),
CardInfo("Raja Yoga","Blue","R","Rajas","14.7","O Arjun, rajo guna is of the nature of passion. It arises from worldly desires and affections, and binds the soul through attachment to fruitive actions.","रजो रागात्मकं विद्धि तृष्णासङ्गसमुद्भवम् | तन्निबध्नाति कौन्तेय कर्मसङ्गेन देहिनम् ||"),
CardInfo("Raja Yoga","Blue","S","Sattva","14.6","Amongst these, sattva guna, the mode of goodness, being purer than the others, is illuminating and full of well-being. O sinless one, it binds the soul by creating attachment for a sense of happiness and knowledge.","तत्र सत्त्वं निर्मलत्वात्प्रकाशकमनामयम् | सुखसङ्गेन बध्नाति ज्ञानसङ्गेन चानघ ||"),
CardInfo("Raja Yoga","Blue","M","Maya","7.14","My divine energy Maya consisting of the three modes of nature is very difficult to overcome. But those who surrender unto Me cross over it easily. ","दैवी ह्येषा गुणमयी मम माया दुरत्यया | मामेव ये प्रपद्यन्ते मायामेतां तरन्ति ते ||"),
CardInfo("Raja Yoga","Blue","Sa","Samsara","9.3","People who have no faith in this dharma are unable to attain Me, O conqueror of enemies. They repeatedly come back to this world in the cycle of birth and death.","अश्रद्दधाना: पुरुषा धर्मस्यास्य परन्तप | अप्राप्य मां निवर्तन्ते मृत्युसंसारवर्त्मनि ||"),
CardInfo("Raja Yoga","Blue","Re","Rebirth","2.12","Never was there a time when I did not exist, nor you, nor all these kings; nor in the future shall any of us cease to be.","न त्वेवाहं जातु नासं न त्वं नेमे जनाधिपाः | न चैव न भविष्याम: सर्वे वयमत: परम् ||"),
CardInfo("Raja Yoga","Blue","So","Soul","2.24","The soul is unbreakable and incombustible; it can neither be dampened nor dried. It is everlasting, in all places, unalterable, immutable, and primordial.","अच्छेद्योऽयमदाह्योऽयमक्लेद्योऽशोष्य एव च | नित्य: सर्वगत: स्थाणुरचलोऽयं सनातन: ||"),
]

def color_to_rgb(color_name):
    colors = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (100, 100, 255),
        "yellow": (255, 255, 0),
    }
    return colors.get(color_name.lower(), (0, 0, 0))

def center_string(s, width):
    zeros_needed = int(width / 2) - len(s) // 2
    if zeros_needed < 0:
        zeros_needed = 0
    return ' ' * zeros_needed + s + ' ' * zeros_needed

def draw_text(img, text, font, position, color):
    d = ImageDraw.Draw(img)
    d.text(position, text, fill=color, font=font)
    return img

def create_base_image():
    width, height = 750, 1127
    return Image.new('RGBA', (width, height))

def draw_background(img, card_info):
    bk_img = Image.open('background.jpg')
    # Loop through each pixel in the image
    # for x in range(bk_img.width):
    #     for y in range(bk_img.height):
    #         # Get the RGB values of the current pixel
    #         r, g, b, a = bk_img.getpixel((x, y))

    #         # Check if the pixel is not white or black
    #         if (r, g, b) != (255, 255, 255) and (r, g, b) != (0, 0, 0):
    #             # Replace the pixel with white
    #             bk_img.putpixel((x, y), (255, 255, 255))





    border_size = 15
  #  bk_img = bk_img.resize((img.width - 2 * border_size, img.height - 2 * border_size))
    seed = (10, 10)
    fill_color = color_to_rgb(card_info.color)
    bk_img = bk_img.convert("RGB")
    ImageDraw.floodfill(bk_img, seed, fill_color)
    text_color = (fill_color[0] - 150, fill_color[1] - 150, fill_color[2] - 150)
    bk_img = bk_img.convert("RGBA")
    img.paste(bk_img, (border_size, border_size))
    return img, text_color

def draw_number(img, card_info, text_color):
    font = ImageFont.truetype('NotoSansDevanagari-Bold.ttf', 80)
    number_text = center_string(card_info.number, 3)
    line_width = font.getsize(number_text)[0]
    number_img = Image.new('RGB', (line_width, font.getsize(number_text)[1]), color=color_to_rgb(card_info.color))
    draw_text(number_img, number_text, font, (0, 0), text_color)
    char_width = int((font.getsize('0')[0]) / 2)
    img.paste(number_img, (char_width, 20))
    number_img = number_img.rotate(180)
    img.paste(number_img, (img.width - number_img.width - char_width, 1040))
    return img

def draw_title(img, card_info, text_color):
    font = ImageFont.truetype('NotoSansDevanagari-Bold.ttf', 60)
    card_info.title = card_info.title.capitalize()
    draw_text(img, center_string(card_info.title, 16), font, (160, 65), text_color)
    return img

def draw_multiline_text(img, lines, font, start_y, text_color):
    y = start_y
    for line in lines:
        line_width = font.getsize(line)[0]
        pos = ((img.width - line_width) // 2+10, y)
        draw_text(img, line, font, pos, text_color)
        y += font.getsize(line)[1]
    return img

import re

def fix_letter_order(text):
  """
  This function fixes the placement of vowel matras at the end of words in Sanskrit text.

  Args:
      text: The Sanskrit text string.

  Returns:
      The corrected Sanskrit text string.
  """
  pattern = r"(\p{L})ि "  # Matches any letter followed by 'ि '
  replacement = r"ि\1 "   # Replaces with 'ि' followed by captured letter and ' '
  corrected_text = re.sub(pattern, replacement, text)
  return corrected_text


def draw_sanskrit(img, card_info, text_color):
    font = ImageFont.truetype('NotoSansDevanagari-Bold.ttf', 35)
    
    sanskrit = card_info.sanskrit

    split_lines = [line.strip() for line in sanskrit.replace('|', '#').replace('||', '#').split('#') if line.strip()]

    lines = []
    intra_split = False;

    box_width = 46 if len(split_lines) > 4 else 38

    if len(split_lines) <= 4:
        for i, line in enumerate(split_lines):
            delimiter = ' I' if i % 2 == 0 else ' II'
            line = line + delimiter
            line_length = len(line)

            # Find space closest to the midpoint
            midpoint = line_length // 2
            closest_space = None
            min_distance = line_length  # Initialize with max length

            for j, char in enumerate(line):
                if char == ' ':
                    distance = abs(j - midpoint)
                    if distance < min_distance:
                        min_distance = distance
                        closest_space = j

            # Split at the closest space
            if closest_space is not None:
                lines.append(line[:closest_space])
                lines.append(line[closest_space + 1:])
            else:
                lines.append(line)  # No space found, use entire line

    else:
        for i, line in enumerate(split_lines):
            delimiter = ' I' if i % 2 == 0 else ' II'
            line = line + delimiter
            line_length = len(line)
            if line_length > 42:
                # Logic similar to above for lines longer than 42 characters
                midpoint = line_length // 2
                closest_space = None
                min_distance = line_length

                for j, char in enumerate(line):
                    if char == ' ':
                        distance = abs(j - midpoint)
                        if distance < min_distance:
                            min_distance = distance
                            closest_space = j

                if closest_space is not None:
                    lines.append(line[:closest_space])
                    lines.append(line[closest_space + 1:])
                else:
                    lines.append(line)  # No space found, use entire line
            else:
                lines.append(line)  # Line length less than 42, use entire line

    padding_lines = 9 - len(lines)
    lines = [" " * (len(lines[0]) // 2)] * (padding_lines // 2) + lines + [" " * (len(lines[0]) // 2)] * (padding_lines - padding_lines // 2)
    return draw_multiline_text(img, lines, font, 180, text_color)

    

def draw_vno(img, card_info, text_color):
    font = ImageFont.truetype('NotoSansDevanagari-Bold.ttf', 35)
    draw_multiline_text(img,['BG '+card_info.vno],font,530,text_color)
    return img

def draw_vdesc(img, card_info, text_color):
    font = ImageFont.truetype('NotoSansDevanagari-Bold.ttf', 35)
    card_info.vdesc = card_info.vdesc.capitalize()
    lines = textwrap.wrap(card_info.vdesc, width=(310) // font.getsize(' ')[0])
    padding_lines = 9 - len(lines)
    lines = [" " * (len(lines[0]) // 2)] * (padding_lines // 2) + lines + [" " * (len(lines[0]) // 2)] * (padding_lines - padding_lines // 2)
    return draw_multiline_text(img, lines, font, 620, text_color)

def draw_yoga(img, card_info, text_color):
    font = ImageFont.truetype('NotoSansDevanagari-Bold.ttf', 60)
    card_info.yoga = card_info.yoga.capitalize()
    draw_text(img, card_info.yoga, font, (150, 1025), text_color)
    return img

# Initialize the list of images
images = []
page_number = 1
import threading
lock = threading.Lock()

def process_card(card_info):
    global images, page_number

    # Create the card image
    img = create_base_image()
    img, text_color = draw_background(img, card_info)
    img = draw_number(img, card_info, text_color)
    img = draw_title(img, card_info, text_color)
    img = draw_sanskrit(img, card_info, text_color)
    img = draw_vno(img, card_info, text_color)
    img = draw_vdesc(img, card_info, text_color)
    img = draw_yoga(img, card_info, text_color)

    # Append the image to the list
    with lock:
        images.append(img)

        # If the list reaches the size of an A4 page, save the page and reset
        if len(images) >= 9:  # Assuming 4 cards fit on an A4 page
            save_page(images, page_number)
            images = []
            page_number += 1

def save_page(images, page_number):
    # Create a new A4-sized page
    page_img = create_base_image()
    page_img_width, page_img_height = 2480, 3508
    page_img = page_img.resize((page_img_width, page_img_height))

    # Calculate the position for each card on the page
    card_width, card_height = images[0].width, images[0].height
    cards_per_row = 3
    card_x = 5
    card_y = 5
    for i, img in enumerate(images):
        page_img.paste(img, (card_x, card_y))
        card_x += card_width + 5
        if (i + 1) % cards_per_row == 0:
            card_x = 5
            card_y += card_height + 5

    # Save the page
    page_img.save(f"gitacards/page_{page_number}.png")
from PIL import Image
import img2pdf
import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def png_to_pdf(folder_path, output_filename):
  """
  Converts all PNG files in a folder to a single PDF, preserving A4 size (2480x3508 pixels).

  Args:
    folder_path: Path to the folder containing PNG files.
    output_filename: Name of the output PDF file.
  """
  images = [
    Image.open(os.path.join(folder_path,f))
    for f in os.listdir(folder_path) if f.endswith(".png")]

  resized_images = [i.resize((i.width//3,i.height//3)).convert("RGB") for i in images]

  resized_images[0].save(
      output_filename, "PDF" ,resolution=100.0, save_all=True, append_images=resized_images[1:]
  )

def fix_letter_order(text, d):
    corrected_words = []
    for word in text.split(d):
        # Check if the word ends with the matra
        if word and word[-1] == "ि":
            # Swap the matra with the second-last character (if it exists)
            if len(word) > 2:
                c = word[-2]
                corrected_words.append( word[:-3] + "ि" + c)
            else:
                # Handle single-character words (leave matra as is)
                corrected_words.append(word)
        else:
            corrected_words.append(word)
    return d.join(corrected_words)

import shutil
def main():
    i = 0
    # Create a new directory
    new_dir = "gitacards"
    shutil.rmtree(new_dir, ignore_errors=True)
    os.mkdir(new_dir)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for card_info in card_deck:
            card_info.sanskrit = fix_letter_order(fix_letter_order(card_info.sanskrit,' '),':')
            # print(card_info.title,card_info.sanskrit)
            executor.submit(process_card, card_info)
    png_to_pdf(new_dir,'gc.pdf')

if __name__ == "__main__":
    main()
