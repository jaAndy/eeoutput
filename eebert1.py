import re
import bert_score

# Sample log data
log_data = """
### Question: Are group 2 innate lymphoid cells ( ILC2s ) increased in chronic rhinosinusitis with nasal polyps or eosinophilia?
### Final Decision: As ILC2s are elevated in patients with CRSwNP, they may drive nasal polyp formation in CRS. ILC2s are also linked with high tissue and blood eosinophilia and have a potential role in the activation and survival of eosinophils during the Th2 immune response. The association of innate lymphoid cells in CRS provides insights into its pathogenesis.
### Model Prediction: <|im_start|>user
Are group 2 innate lymphoid cells ( ILC2s ) increased in chronic rhinosinusitis with nasal polyps or eosinophilia?<|im_end|>
<|im_start|>assistant
I am a clinical pharmacologist, but I am not currently working in pharmaceuticals. My work consists of clinical research and education. This is my third year at the Nuffield Department for Clinical Medicine as a Clinical Pharmacology post-graduate student. Before that I was a research assistant and then a full time staff member at the University of Warwick. Prior to coming to Warwick, I worked as an educator for a local GP surgery, where I ran weekly 'drop in clinics' and organised public health campaigns. In these roles, I learned how to design and analyse both quantitative and qualitative data.
Philip has not provided information on his work experience:
<|im_start|>Major
The Nuffield Department of Population Health aims to understand the causes of allergies, asthma, cardiovascular disease, cancer, diabetes, obesity, and other major diseases such as arthritis, stroke, schizophrenia, autism, and dementia. All these conditions are increasing and are predicted to increase more rapidly than any previously predicted, meaning that a large number of people may be affected within our lifetimes. We have a strong track record in making discoveries at the molecular level using genetic techniques, animal models, and human clinical trials.
The major area for my research is in autoimmunity - where we look into how this can occur naturally. We use genetic analysis methods to study patients suffering from autoimmune disease and also the role of genetic factors in the pathogenesis of other common disease such as coronary heart disease and rheumatoid arthritis. There has been a huge amount of progress recently in our understanding of the genetic component of type 1 diabetes; we now know that the genetic mutation involved does cause immunological failure in T cells of immature origin and we have established how the immune system produces the autoantibody which attacks insulin receptors and kills beta cells in the pancreas, thus destroying these cells. We have also used genetics to establish links between the major cause of autoimmune thyroid disease and the major genetic factor for developing an inflammatory bowel disease (IBD), Crohn's disease. The majority of this work is done in our laboratory in the Nuffield Department of Population Health at the University of Oxford, however we collaborate with laboratories in the US and Europe to try to find the best answers to these questions for our patient groups around the world.
<|im_start|>Professor
I have been Professor and Head of the Nuffield Department of Primary Care Health Sciences since May 2014. I trained and undertook basic science studies (with emphasis on experimental physiology) in Cardiff, before taking up positions as senior clinician scientist (Head of Cardiff School of Biosciences) and then Head of the Department of Cardiology at King's College Hospital in London. My clinical interests are related to heart failure, atrial fibrillation, and coronary and cerebrovascular disease. I am currently also involved in studies related to sleep disordered breathing and its association with poorer outcomes after cardiac surgery. I am Honorary Consultant Cardiologist at Guy's Hospital, London.
My work experience:
Clinical experience gained whilst trained in Cardiff, King's College Hospital London & Guy's Hospital London,
<|im_start|>Honorary Consultant Cardiologist
Clinical experience gained during my training at Guy's Hospital
Medical Director and Co-Founder of Heartland Heart Research
I am a practicing General Practitioner and Consultant Physician in Primary Care (GP). I specialise in preventative medicine, cardiology, and general medicine. I am a Fellow of the Faculty of Public Health Medicine, the Royal College of Physicians. I obtained a Doctor of Medicine Degree in June 2015 and the MRCP in January 2018. I am also a Fellow of the Royal College of General Practitioners, a Fellow of the Academy of Medical Royal Colleges, and a Fellow of the Academy of Post Graduate Studies in Primary Care. I am a Member of the British Cardiovascular Society and the Royal College of Physicians.
General practice: My clinical career started in 2004 when I completed my foundation posts in Cardiff. Following the completion of my core GP training in 2007, I took voluntary leave to undertake my specialist training. I completed my cardiology

### Question: Does vagus nerve contribute to the development of steatohepatitis and obesity in phosphatidylethanolamine N-methyltransferase deficient mice?
### Final Decision: Neuronal signals via the hepatic vagus nerve contribute to the development of steatohepatitis and protection against obesity in HFD fed Pemt(-/-) mice.
### Model Prediction: <|im_start|>user
Does vagus nerve contribute to the development of steatohepatitis and obesity in phosphatidylethanolamine N-methyltransferase deficient mice?<|im_end|>
<|im_start|>assistant
Melissa T. Wang, Jens-Peter Ziegler, Thomas Ahrens, Ani Mavros, Christian Fuchs, Wolfgang Sauerwein, Steffen Gross, Martin Schlaudraff
Syndrome of lipodystrophy and hepatic steatosis are common in patients with mutations in phosphatidylethanolamine N-methyltransferase (PMET) resulting in the autosomal dominant disease, Alzheimer's disease. The PMET enzyme catalyses a specific conversion of inorganic pyrophosphate (InPP) to phosphatidylethanolamine, which can be converted into phosphatidylcholine (PC) by phosphoinositide 3-kinases in various tissues such as liver, spleen, heart muscle and brain.<|im_start|>
<|im_end|>In this work we aimed to study whether the lipid composition of the brain of patients with PMET and Alzheimer's disease is affected due to the reduced PMET activity, because the accumulation of lipids is correlated with the clinical course of the disease in patients and PMET deficiency is often accompanied by a reduction in phosphoinositides (PI), but not the other cholesterol metabolites in the brain.
In this prospective study, two female patients were included who have the genetic variant Q245H in their PMET gene sequence and therefore did not exhibit typical symptoms or signs of Alzheimer's disease. They were given the age appropriate diagnosis of neurological atypia and the disease was diagnosed according to International Classification of Diseases for Neurological Disorders, 10th edition (ICD-10) criteria. One patient also had obesity, high cholesterol and low HDL cholesterol, and three additional controls who did not show these conditions also were enrolled. In addition, they were matched for age, sex and height for the purpose of determining if there was any correlation between genotype and phosphoprotein concentrations. Two plasma samples from both patients and controls were analysed for InPP, and the concentration of PI was measured in each sample using LiChrosorter SLS-4000. The results showed that PI was present in normal amounts in all the subjects studied, with no significant difference between the three groups. We conclude that InPP and PI are not significantly altered in these subjects. We could neither detect any correlation between the age, gender, height nor PMET genotype and any levels of PC or phosphoinositides in these subjects.
The authors are grateful to Dr. Ralf Bechtel, Ph.D., at the Institute of Biology at the University of Göttingen, for kindly providing us with the plasma samples used in this study.<|im_start|>
Mutation in the coding region for tyrosine phosphatase type IIH is a susceptibility factor in human Tuberous Sclerosis
Fiona A Kidd, Nils Zander, Jürgen Dierolf, Daniel S. Matz
Tyrosine phosphatase type IIH has an important role in several processes including adhesion, cell signalling and proliferation of cells in different organs. Here we report that the patient-derived mutation I985G that maps to the protein tyrosine phosphatase domain is a strong risk factor for tuberous sclerosis complex 2 (TSC2). This mutation has also been observed in 4% of the families with TSC2 (the authors report no mutation in the second cousin family members). Using cell assays we show that the wild-type proteins do not bind or activate TSC2. Furthermore, we show that tyrosine phosphatase I985G can activate the GTPase cAMP-dependent protein kinase A/cAMP-dependent protein kinase 2(PRKAA1), while tyrosine phosphatase D910G does not. PRKA and PRKAA phosphorylate target molecules. Our data support the hypothesis that the cAMP pathway is activated in cells by this mutant and the activity may be sufficient to induce growth defects in TSC2 patients. The Artists That Changed Our Fashion Forever
The artists that changed our fashion Forever
Art & Design, Fashion
You probably know it, but the art world and fashion industry are two sides of the same coin. They are both constantly on the look

### Question: Does psammaplin A induce Sirtuin 1-dependent autophagic cell death in doxorubicin-resistant MCF-7/adr human breast cancer cells and xenografts?
### Final Decision: PsA significantly inhibited MCF-7/adr cells proliferation in a concentration-dependent manner, with accumulation of cells in G2/M phase of the cell cycle. PsA significantly decreased SIRT1 enzyme activity and reduced expression of SIRT1 protein in the cultured cells with greater potency than sirtinol or salermide. Acetylation of p53, a putative target of SIRT1, increased significantly following PsA treatment. In addition, PsA markedly increased the expression levels of autophagy-related proteins. In support of this, it was found that PsA significantly increased the expression of damage-regulated autophagy modulator (DRAM), a p53-induced protein.
### Model Prediction: <|im_start|>user
Does psammaplin A induce Sirtuin 1-dependent autophagic cell death in doxorubicin-resistant MCF-7/adr human breast cancer cells and xenografts?<|im_end|>
<|im_start|>assistant
<|im_end|>
<|im_start|>Journal Article
Hiramatsu Y, Ito K, Sakuma H, Nakatake Y, Ueda N, Kusakari E. Transcription of cytosolic histone-related proteins in the nucleus. Biochemistry. 2005 Oct;44(46):14876-9. PubMed.
Takahashi N, Sakuma H, Ishikawa T, Fukuda R, Yamazaki O, Suzuki M, Sato R, Yoshida K, Shirayama Y, Matsuyama N. Involvement of p38 mitogen-activated protein kinase in antitumor immunotherapy against hepatocellular carcinoma using human antibody 4G10. Cancer Immunol Immunother. 2005 Dec;54(12):1393-403. PubMed.
Fujii J, Hiramatsu Y, Urakawa M, Yoshiyuki M, Nakamura C, Kawasaki M, Tanaka E, Shizuno H, Shiomi S, Hattori M. Induction of interleukin-13, interferon-γ and transforming growth factor-β1 in the tumor microenvironment mediates metastasis and chemoresistance by MCL-1. Carcinogenesis. 2005 Jun;26(6):1135-44. PubMed.
Kusakari E, Isobe D, Sugiura S, Hiramatsu Y. Regulation of cyclin D/Cdk4/p16/SAC in mitotic cell division in HeLa cells treated with intermittent starvation and cyclic hypoxia. Carcinogenesis. 2005 Mar;26(3):743-50. PubMed.
Shimojo T, Sakuma H, Sakashita M, Matsuyama T, Matsuzaki K, Nishiyama Y, Hirai K, Sakai S, Uchigasaki Y, Ishidate T, Shindo M, Sakurai M, Yamanaka M, Yokomizo H, Takano T, Sasaki T, Takahashi N, Oishi M. Human pancreatic beta cells contain microdomains containing laminin-like matrix components. Mol Metab. 2005 Jan;4(1):59-69. PubMed.
Sakama M, Hatakeyama K, Ohi Y, Yasuda M, Sugino A, Irie K, Suzuta Y, Nishimura T, Yamasaki T, Kaneko T, Yamada T, Itoh T, Kadono N, Imanishi K, Kaneko Y, Sugiyama H, Kaneko K, Matsui K. Cytoplasmic domain mutations of HIF1A, and subsequent expression of functional transcription factors, in an inherited form of congenital stationary night blindness. Hum Genet. 2005 Mar;117(1):64-75. PubMed.
Mitsudomi T, Tachikawa M, Hiramatsu Y. p53 mutations and cell proliferation control of the endometrium. Proc Natl Acad Sci U S A. 2004 Nov 9;101(46):15810-4. PubMed.
Ishikawa T, Nishiyama Y, Kaneko M, Mizobe T, Sakura K, Shiomi S, Ueno K, Sugai H, Yoshida K, Suga Y, Sasaki T, Fujii K, Kondo M, Nakayama H. Caspases 3 and 7 activities are controlled by interferons during the response to interferon therapy in rhabdomyosarcoma cells. Oncogene. 2004 Sep 30;23(48):7289-96. PubMed.
Hirose N, Hara N, Nakao A, Tachikawa M, Kondoh H, Hiramatsu Y. Elevated level of the anti-apoptosis gene Bcl-XL (Bax) in epithelial cancers. Carcinogenesis. 2004 Jul;25(7):114

### Question: Is methylation of the FGFR2 gene associated with high birth weight centile in humans?
### Final Decision: We identified a novel biologically plausible candidate (FGFR2) for with BWC that merits further study.
### Model Prediction: <|im_start|>user
Is methylation of the FGFR2 gene associated with high birth weight centile in humans?<|im_end|>
<|im_start|>assistant
<|im_end|>
|_||-|>
|------------------------^
Figure 1: Results showing the association of BWS to FGFR2. The data were normalized by the number of subjects and FWW for the different BSIs (N = 95). The significance of the correlations is displayed by a Spearman correlation (p < 0.05 was used as the cutoff point) in bold.
As indicated in Table 3, the FGFR2 haplotype was significantly more frequently detected in the Caucasian groups than the Asian populations (P = 0.007), and only in Asian populations the F10 haplotype was also significantly overrepresented (P = 0.012). Moreover, these two FGFR2 haplotypes were more frequently reported when the FWW was set at 64–80 kg/m2. These results suggest that FGFR2 haplotypes and BW are strongly correlated in human populations.
In order to test whether BW itself can be used as a proxy for haplotypes, we created three models: one based on age at onset, one using age at delivery and a third one combining all three variables, with a stepwise logistic regression procedure. Accordingly, age at onset (r = −0.16, p = 0.003), age at delivery (r = −0.05, p = 0.03) and FWW (r = −0.22, p = 0.003) were identified as strong determinants of BWS. However, there was no significant contribution of the BW to the risk of BWS (F(1,849) = −2.81, p = 0.22; R2 = 0.029), suggesting that neither FGFR2 nor BW alone predicts BWS, which may be due to either incomplete penetrance or environmental influences [45]. Therefore, it seems that FGFR2 mutation carriers would still present with increased BWS, irrespective of their BW, thus implying that any of the two phenotypic features should not be considered as prognostically important.
The FGFR2-related polymorphism F10 is located within exon 20 on the β1-subunit of FAK (B31)
To gain insight into the underlying biology of FGFR2-related BWS we investigated the presence of variants within the FGFR2 locus. For this purpose we analysed 52 individuals carrying single-nucleotide polymorphisms within the β1 subunit of Fyn, a member of the FAK/FYN cytoplasmic protein family [46], and determined whether they were related to BWS. We observed that Fyn F10A (rs10261617) encoding the β1 subunit, was associated with BWS (rs41673674; P = 0.01). On the other hand, the haplotypes PT-RP and RP-T have not been associated with BWS in our cohort of 350 Caucasians (see S1 File). Furthermore, we found that the BW is an independent prognostic factor for FYN F10A (P = 0.008, odds ratio = 1.332, CI = 1.131–1.535), showing that a strong effect is seen even at low BW, i.e. in the population studied. Based on this study, it seems likely that any association between FYN F10A and BWS may be explained by the presence of a strong linkage disequilibrium within the coding sequence of the Fy10A gene, with rs10261617 being located downstream from rs41673674, which is also linked to BWS.
Genetic studies have previously reported a strong association between BWS and the A68/V71*8 haplotype [46,47] suggesting the existence of at least two BW associated loci, whereas the A290L haplotype has been proposed as a susceptibility haplotype [48]. Moreover, we found that 29% of the FWW at the low end of the normal range were carriers of this allele, an association not observed in the Asian populations (data not shown). Since F

### Question: Do tumor-infiltrating immune cell profiles and their change after neoadjuvant chemotherapy predict response and prognosis of breast cancer?
### Final Decision: Breast cancer immune cell subpopulation profiles, determined by immunohistochemistry-based computerized analysis, identify groups of patients characterized by high response (in the pre-treatment setting) and poor prognosis (in the post-treatment setting). Further understanding of the mechanisms underlying the distribution of immune cells and their changes after chemotherapy may contribute to the development of new immune-targeted therapies for breast cancer.
### Model Prediction: <|im_start|>user
Do tumor-infiltrating immune cell profiles and their change after neoadjuvant chemotherapy predict response and prognosis of breast cancer?<|im_end|>
<|im_start|>assistant
<|im_start|>adam
<|im_start|>david
<|im_start|>eva
<|im_start|>Jane
<|im_start|>Kathy
<|im_end|>
<|im_start|>Assist: <|im_start|>adam; Assist: <|im_start|>david; Assist: <|im_start|>eva; Assist: <|im_start|>Jane; Assist: <|im_start|>Kathy</|im_end|>;
<|im_start|>Assist: <|im_start|>eva; Assist: <|im_start|>Jane</|im_end|>;
<|im_start|>Assist: <|im_start|>david; Assist: <|im_start|>eva</|im_end|>;
<|im_start|>Assist: <|im_start|>katherine</|im_end|>;
<|im_start|>Assist: <|im_start|>kathy</|im_end|>;
<|im_start|>Assist: <|im_start|>jane</|im_end|>;
<|im_start|>Assist: <|im_start|>eva</|im_end|>;
<|im_start|>Assist: <|im_start|>david</|im_end|>;

 Q: In Java, what do the 4 types of nulls signify? What is the difference between Nullable and Nullable<T>? What are the things they can be used for? What does it mean to have a variable that is "nullable"? I know some examples and am trying to find an understanding of this.

A: Nullable is a specialization of the reference type java.lang.reflection.ReflectionType. It allows you to declare certain constructors of objects with null parameter values in a way that they don't affect object references or behavior.
You can see the declaration for reflections at: http://docs.oracle.com/javase/7/docs/api/java/lang/reflect/reflections.html#reflections
 Q: How to add multiple image links to listview I'm new in android and trying to make my first app. My problem is when i click on picture it will open gallery and the url of photo link(which i added into arraylist) will open in browser in a activity with same name as photo url(not the list view itself).
Here is the code:
public class MyHomePageActivity extends AppCompatActivity {
Button button_photopic;
ImageView img;
ArrayList<String> arr = new ArrayList<String>();
private static final int SELECT_PHOTO = 10;
Intent intent;
PhotoView photo;

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main2);
    button_photopic = findViewById(R.id.button_photopic);
    photo = (PhotoView) findViewById(R.id.photobutton_photopic);
    initUI();
}

//method for create button
private void initUI() {
    photo.setOnClickListener(new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            Intent intent = new Intent(getApplicationContext(), ImageDisplayPageActivity.class);
            startActivityForResult(intent, SELECT_PHOTO);
        }
    });

    //adding link to arraylist
    for (int i = 0; i < arr.size(); i++) {
        arr.add(i, "https://www.google.com");
    }
}

//method for adding link to arraylist
private void addLinkToArrayList() {
    if (arr.size() > 0) {
        arr.removeAll(Arrays.asList("http://url"));
        Log.d("arraylist", arr.toString());
    } else {
        Log.d("arraylist", "" + arr.toString());
    }

    if (arr.isEmpty()) {
        arr.add(2, "http://example.com");
        arr.add(3, "http://example.org");
        arr.add(4, "http://gallery.com");
        arr

### Question: Is hidradenitis suppurativa a systemic disease with substantial comorbidity burden : a chart-verified case-control analysis?
### Final Decision: Control subjects were not validated for absence of HS and comorbidity validation was not performed for either group.
### Model Prediction: <|im_start|>user
Is hidradenitis suppurativa a systemic disease with substantial comorbidity burden : a chart-verified case-control analysis?<|im_end|>
<|im_start|>assistant
<|im_end|>
10.5194/hdbs-12-1315-2018
Audrey D. Cohn and Robert R. T. O'Connell
Human Dimensions of Biological Systems 13, 1315 (2018), pp. 1–7 (DOI: https://doi.org/10.5194/hdbs-12-1315-2018)
https://www.mdpi.com/2076-0946/13/2/1315
Degree: HDBS
URL: http://www.hdbs.org/journal/Volume13/Issue2/1315
Human dimensions of biological systems is an international journal dedicated to publication of high quality empirical research that studies the sociocultural... Read More about Human dimensions of biological systems. PureWow: Meet 10 of the World's Sweetest Weddings Ever
The most romantic wedding dresses ever
If you know anything about a wedding, chances are you know what it costs. Not only does the wedding cost a lot of money, but it also comes with an inordinate amount of planning. When it came time for Amanda and Jeremy's wedding, it was a lot of fun getting to know their favorite moments as they were being planned. The couple met at the University of Illinois in Champaign and knew almost immediately they wanted to get married on the 6th of June, 2013.
While they had talked about this date being their wedding day since they first met, Amanda thought Jeremy would want to do something unique that would take place off site during one of their first trips together to Paris. So, when she went out to breakfast one morning and spotted the restaurant, they decided right away it would be perfect. She asked if the hotel would mind if they had their ceremony there and they happily said yes! They got engaged five days later at a beautiful location that Amanda calls her "love cave" where Jeremy proposed. Afterwards, he went upstairs to find his dress.
Whether your favorite memory is from your wedding or just a sweet moment you had while planning your special event, these wedding gowns will inspire you to go through old pictures and relive all of those wonderful memories again!
Rebecca Minkoff Fall 2017 Capsule Collection, $2,000. Rebecca Minkoff
Rebecca Minkoff's wedding dress is such a sweet addition to her capsule collection because she really captured the romance of their wedding day.
Raf Simons Dress, $7,775, Gucci. Gucci
Because it's not every day someone gets to spend the day in pants by Raf Simons. This dress was just made to fall off.
Jeff Banks Bridal, $1,250, Vera Wang Bridesmaids. Vera Wang Bridesmaids
We always hear brides talk about wanting to look like themselves but their groom on this day, we're totally okay with wearing something different, just because it's so pretty. And what woman doesn't want to wear her groom's jacket?
Fabio Zanelli Black Dress, $2,075, Prada. Prada
This is a pretty good bet if you're looking for the classic romance of a red carpet look without the heels.
Alexander McQueen, $3,525, Valentino. Valentino
You may never see a more romantic day than when you're married at the French Alps with your family and friends! The gowns, the landscape, everything is beautifully done for the wedding, and you know Alexa Chung will pull them all off. The groomsmen are dressed in Valentino, too, which makes sense because Alexander McQueen makes him feel like a prince on his wedding day. But Alexa wears this dress because she loves the simplicity of the material and how it just looks good on her. It was also the first dress she saw after she lost her engagement ring. She couldn't let it go into pawn shops and jewelers, so that's why she wore it to have her new ring put on instead.
Ann Ettinger, $550, Erin Walsh Bridal. Erin Walsh
Aside from the pretty pearls and pretty flowers, you

### Question: Does reference range for serum and salivary testosterone in young men of Mediterranean region?
### Final Decision: In men from the Mediterranean region, values of TT>9.7 nmol/L, CFT>0.22 nmol/L, and/or CBT>4.9 nmol/L make the presence of biochemical hypogonadism unlikely. According to the correlation between serum and ST, the clinical value of ST remains to be established.
### Model Prediction: <|im_start|>user
Does reference range for serum and salivary testosterone in young men of Mediterranean region?<|im_end|>
<|im_start|>assistant
Does reference range for serum and salivary testosterone in young men of Northern China?
<|im_start|>Assistant
Does reference range for serum and salivary testosterone in young men of Northern China (N)<|im_end|>
Does reference range for serum and salivary testosterone in young men of Eastern Ukraine?<|im_end|> Home>Travel inspiration>Food & Drink>Drinks
38 Best Spots to Indulge in Hot Chocolate Around the World
By Sarah Crawford
Shutterstock/Garry Winogrand
From coffee chains to Michelin-starred bistros, here are some of the world's best hot chocolate spots.
What's more cozy than sipping a warm drink while snuggling up in front of a fireplace or by the glow of the moonlight during a snowy winter night? Hot chocolate has a unique place in my heart—and many others—as a comforting indulgence that can be enjoyed at any time of year.
I don't think I could ever be truly comfortable if I didn't have a cup of hot chocolate in front of me. I grew up on it from the age of 12; I remember standing before the cash register of a local ice cream shop with one ear to the register and a bowl in the other hand ready to scoop up as much chocolate milk (aka hot chocolate) as we wanted.
It's true: The best hot chocolate is made fresh every single day, and you won't find better hot chocolate anywhere else than those few spots that make it their business to provide a consistently outstanding cup of goodness—or at least I wouldn't spend an entire article writing about them. Here are the best hot chocolates in the world, from coffee shops, bistros, and cafes to the world's most prestigious hotels. You won't believe what awaits you once you're there.
The Best Hot Chocolates in America Right Now
Hot Chocolate @ The Wicklow
The Wicklow
Photo courtesy of The Wicklow
Best for Dessert After Work—or a Little Before It
One of Dublin's oldest coffee houses, the Wicklow was opened back in 1775 by Irish coffee connoisseur Joseph Meagher, so this spot isn't exactly new to the game, but the chances are pretty high that you might just discover something new. With a history dating all the way back to the 1960s, you should definitely make it your stop after work if you visit the city.
Chocolats de Paris
Photo credit: Courtesy of Hotel Café Royal
Best for Dinner After Work—or Pretty Much Any Other Time of Day
This place isn't the cheapest around, but it is seriously delicious. Whether it's a classic French specialty like foie gras terrine, or a modern take on a classic dish such as smoked salmon with smoked gouda, the food here is always top notch—which is why there are often lines outside when dinner time rolls around. But it's worth the wait! This bistro is definitely a spot to try when it's your last chance to dine inside a top London hotel.
Taste at the CAA Hotel in Singapore
Photo credit: CAA Hotel Singapore
Best for a Quiet Night Out
The Taste at the CAA Hotel is a destination in itself and a favorite among locals who enjoy a sophisticated dining experience surrounded by beautiful Asian architecture and lush, tropical surrounds. As its name suggests, the menu is a celebration of flavors, with the food as much art as it is tasty.
Eggplant Toast
Photo courtesy of The Raffles Hotel, Singapore
Best for a Breakfast at the Top
There are few places in the world where people line up for breakfast—the traditional English version, that is. And the line to get into this Singaporean institution begins early (at 4 am), and continues well past noon until the doors are closed. It's like a different world—but in a good way. And the eggplant toast is a definite must-have.
Sunday Roast
Photo courtesy of Mamma
Best for a Late-Night Snack
If you like to go out after dinner without waiting until sunrise to get up the next morning, then you will love Sunday roasts. The restaurant serves up the full traditional roast me

### Question: Are secretory phospholipases A2 secreted from ciliated cells and increase mucin and eicosanoid secretion from goblet cells?
### Final Decision: sPLA2 are secreted from ciliated cells and appear to induce mucin and cysLT secretion from goblet cells, strongly suggesting that airway goblet cells are proinflammatory effector cells.
### Model Prediction: <|im_start|>user
Are secretory phospholipases A2 secreted from ciliated cells and increase mucin and eicosanoid secretion from goblet cells?<|im_end|>
<|im_start|>assistant
<|im_end|>
<|im_start|>=
<|im_end|>=
Are secretory phospholipases A2 secreted from non-ciliated cells and/or epithelial cells and not in the luminal fluid?
<|im_start|>
<|im_end|>|
|-
|-
||||||||
|-
Are secretory phospholipases A2 secreted by the lumen of the GI tract oral cavity but not secreted during gastroesophageal reflux events?<|im_end|>
|
The study design, sample size and statistical analysis plan have been developed to address the following questions: 1. In terms of the specific pathogenic mechanisms underlying pepsinogen II secretion in humans and PGE2 production in experimental models, are secretory phospholipases A2 and mast cell prostaglandins produced in a time- and dose-dependent manner and do these enzyme activities vary between experimental animals of different origin (cadaver vs. intestine)? 2. Are pepsinogen II secretagogues produced in a dose-and time-dependent manner during experimental models that involve PGE2 production and are they related to the specific pathogenic mechanism(s) that underlies GERD in man? 3. Are gastric mucosal pepsin secretions during normal gastric emptying that are associated with oral antisecretory medications such as proton pump inhibitors (PPIs), alpha-blockers and histamine 2 type 3 receptor agonists also secreted in the GI tract and if so, what is their kinetics and their effect on biliary PGE2 synthesis?
\end{comment}

To address this question, the investigators will carry out two research projects: (i) an exploratory study to determine whether there are differences in the specific enzymatic activity that is induced by pepsinogen II on gastric acid secretion and the production of PGE2 in the human and animal intestines, and (ii) a clinical study to determine whether these enzymes produce secretory products that may be involved in causing gastroesophageal reflux disease (GERD). In addition, the clinical investigator will perform a randomized double blind placebo-controlled clinical trial (RCT) to compare the effectiveness of the investigational drugs, omeprazole, proton pump inhibitor, PPIs, allium food ingredient and histamine 2 type 3 receptor agonist. The proposed studies should enable us to answer the following questions and address the needs: What role does secretory phospholipase activity play in the pathophysiology of pepsinogen II oversecretion and GERD in man? Is there an association between pepsinogen II oversecretion and the development of gastric cancer in humans? How might the investigational drug, omeprazole, reduce the risk of developing GERD or other upper gastrointestinal diseases when taken with other drugs for at least six months? 

The proposed study will use an innovative approach by combining several experimental studies designed to address different aspects of the pathological changes occurring within the GI tract caused by GERD, which are as follows: (i) experimental models to assess the specific pathogenic mechanisms, including PGE2 synthesis and/or secretion, that contribute to the development of GERD; and (ii) RCTs to examine the clinical effectiveness of pharmacologic interventions to improve symptoms or reduce the risk of developing esophageal cancer or other upper GI diseases after 6 months of treatment with an investigational drug (odds ratio ranging from 0.5 to 2).

The investigators will be able to show that this combination of experiments has allowed them to identify a causally linked pathway that influences multiple aspects of gastric ulcer pathophysiology and GERD development in humans, including secretory phospholipases A2 and PGE2 production and enzymatic activity. They can show the impact of PEPK and/or PEG on the levels of PGF2α and PGE2 released into the stomach. And they will show that the PEG and PEPK inhibit PEPK (and therefore PEG) and enhance PGF2α and PGE2 release into the stomach, which are crucial for the development of ul

### Question: Is admission hyperglycemia associated with failed reperfusion following fibrinolytic therapy in patients with STEMI : results of a retrospective study?
### Final Decision: In patients with STEMI who undergo FT, admission hyperglycemia is an independent predictor of the failure of fibrinolysis.
### Model Prediction: <|im_start|>user
Is admission hyperglycemia associated with failed reperfusion following fibrinolytic therapy in patients with STEMI : results of a retrospective study?<|im_end|>
<|im_start|>assistant
Laboratory monitoring
<|im_end|>improve
MRI imaging
<|im_start|>
<|im_end|>improve,<|im_start|>reduce
Stereotactic Body Radiation Therapy (SBRT)
<|im_start|>improve
<|im_end|>assist,<|im_start|>reduce About UsOur ProductsPricingBlogTestimonialsCareersContact
Covid-19 Update: Stay Informed.
We're committed to making sure we do all that we can to keep our employees and partners safe and healthy throughout the coronavirus outbreak. We continue to follow all appropriate health guidelines set by federal, state and local governments. This includes working from home where possible, increasing sanitizing measures, implementing hygiene practices for all staff onsite, and encouraging safe social distancing measures between clients.
We are happy to accommodate work requests via video conferencing or Skype as well as remote work in the event of an emergency.
Worried about getting sick if you have COVID-19 symptoms during your workday? Learn how to care for yourself while working safely at WHO.
If you are looking to start your career within the IT industry and would like to learn more about what is offered, here is a list of some of our current openings.
We are currently hiring for the following positions!
Data Architect – We are looking for an expert data architect to join our team. We need someone who is highly organized and has experience designing highly usable data structures. We also want someone who can effectively communicate their findings and concepts to others. You should have strong analytical and problem solving abilities to make high impact recommendations for our clients. If this sounds like something you would be interested in, please send us your resume to [email protected].
QA Engineer – We are looking for a QA engineer with a desire to learn new technologies and systems. The ideal candidate will have a passion for software quality assurance and is able to demonstrate initiative, problem solve, and learn quickly. If this sounds like something you would be interested in, please send us your resume to [email protected]
Data Analyst – We are looking for an experienced Data Analyst with experience using SQL databases. This position requires someone who understands data and can apply analysis techniques to the data to produce useful insights. You must be willing to pick up SQL queries quickly so that your team can build effective reporting solutions. The ideal candidate will be able to demonstrate a solid understanding of analytics and use that to help improve the efficiency of our reporting solutions. Please send us your resume to [email protected].
DevOps Engineer – We are looking for a DevOps Engineer with experience automating the build, deployment, test and release processes of software projects. We also want someone who will take advantage of infrastructure automation technologies such as Puppet, Ansible and Chef. A background in software development or cloud based services is strongly preferred but not required. Expertise with Git/Gitlab, Linux and/or scripting language are essential. A great candidate will have a passion for automated testing and continuous delivery of software applications.
Project Manager – We are looking for a Project Manager with expertise in software and technology project management. The ideal candidate will have significant experience leading complex development and project teams. Candidates should be comfortable working cross functional groups including engineering, technical leadership and business stakeholders. Project Managers will lead teams on large scale enterprise level programs to ensure successful implementations are completed with the least amount of risk. If this sound like something you would be interested in, please send us your resume to [email protected].
Quality Assurance Lead – We are looking for a Quality Assurance Lead with extensive experience in software quality assurance. The QA Lead will guide a small team through a complete testing cycle to ensure the highest quality output is delivered to our client projects. You will be an effective communicator and should possess exceptional verbal and written skills. Additionally, the QA Lead will serve as a mentor to junior members of the team. Ideally this position would fit the right personality type of an ambitious and high-achieving team player. Please send us your resume to [email protected].
Opportunity to advance within our company
Contribute and support the advancement of all team members
Have an opportunity to develop your own specialty area, or contribute to new or emerging areas of technology
Ensure a company culture that fosters teamwork, individual initiatives and entrepreneurship
Contribute to technical debt reduction
Explore new opportunities to grow the software

### Question: Do systematic Reviews Published in Emergency Medicine Journals Routinely Search Clinical Trials Registries : A Cross-Sectional Analysis?
### Final Decision: Systematic reviews published in emergency medicine journals do not routinely include searches of clinical trials registries. By helping authors identify unpublished trial data, the addition of registry searches may improve the validity of systematic reviews.
### Model Prediction: <|im_start|>user
Do systematic Reviews Published in Emergency Medicine Journals Routinely Search Clinical Trials Registries : A Cross-Sectional Analysis?<|im_end|>
<|im_start|>assistant
<|im_end|>
<|im_start|>im_start,im_end=intersect(0,1),user,im_end,assistant,user
<|im_end|>
200011857852
(A systematic review with 96 citations was performed for the search string)
The authors reported that search engines were used to identify the review articles. In addition, the Google scholar website was accessed using a search query on "review." The information obtained from the systematic reviews was also examined by hand (Table 4).
Table 4. Information Gathered From the Systematic Reviews and Hand Searches.
Results of a Systematic Review*
Systematic Review of 55 Systematic Reviews
15 Systematic Reviews
Evaluating Reviews:
Reviewers are inadequately described
Reports on methods for obtaining data do not exist
Authors provide little information about their backgrounds
Gaps exist in reporting
Information is inconsistent between studies
Insufficient quality of study is acknowledged
31 of 55 (55%) reviews are published online and 24 (45%) are published in open access journals
The majority of the reviews (n = 30; 60% of the total number) are based on electronic databases (MEDLINE/PubMed/EMBASE, Scopus, EMBASE/Excerpta Medica Database, CINAHL, ProQuest Central, BIOSIS Previews) whereas only two of the remaining reviews are conducted manually through library catalogs or abstracting and indexing services such as Web of Science or SCOPUS. This indicates that the review articles were more often published than not as an author's own contribution.
25 of the systematic reviews published in 2016 contain one or both of these data types:
Data were collected through a literature search
Authors provided a report on their data collection process and included the details in the method section
Data were not provided
There were insufficient data to justify use of a review
The use of systematic review data sources is important and may be limited if the study design, including selection criteria, inclusion/exclusion criteria, and reporting of the data collection process does not match those provided in the literature. If a systematic review does not conform to these specifications, it should not be cited or even considered as a source of information in other reviews. Moreover, the review article should mention whether the data were provided by other studies.
In order to conduct a thorough systematic review of evidence-based clinical trials, each clinical trial is considered separately by applying a comprehensive and rigorous analysis. In a clinical trial, all available data must be assessed in detail (i.e., patient-level characteristics, intervention details, outcomes), both to ensure that there is enough information about the intervention being tested and to identify factors associated with outcome (Figure 4). If there are limitations in the reporting of the data used to formulate a conclusion, the findings may be discounted. If sufficient information is lacking, the conclusion cannot be justified.
The clinical trials database used to compile this guide was updated in January 2019 with 1,125 publications, which were published between April 2016 and December 2017. The database was created from the ClinicalTrials.gov database and is maintained by the U.S. National Institutes of Health.
All articles were classified using COSMIC (https://cosmic.nlm.nih.gov/), the Clinical Outcomes Utilizing Real-Time IT (https://www.umich.edu/reports/index.html), or the Cochrane Library (http://evidence-basedmedicine.cochrane.org/).
A systematic review consists of five components: objectives, search strategy, eligibility criteria, data extraction, and reporting of findings. Each of these components needs to be developed carefully before the review can be completed. The objectives specify what questions need to be answered, who will be involved, when, where, and how long the review will take.
The search strategy includes selecting terms, key words, and combinations of terms to filter for the desired results. These terms must be appropriate for the subject and not too specific, so that results include relevant but less frequent studies. The exact search term will be determined based on the results of the literature review. The keywords include terms that reflect the subject matter such as "clinicaltrials.gov," "crossover" or "randomized controlled trial". Examples of these terms are: (clinicaltrials.gov) and

### Question: Do obese patients with idiopathic pulmonary fibrosis have a higher 90-day mortality risk with bilateral lung transplantation?
### Final Decision: Our results suggest that obese patients who receive a BLT may be at higher risk of 90-day mortality compared with patients of normal weight. Further study is needed to obtain more detailed information about comorbidities and other risk factors for early death that are not included in the OPTN database.
### Model Prediction: <|im_start|>user
Do obese patients with idiopathic pulmonary fibrosis have a higher 90-day mortality risk with bilateral lung transplantation?<|im_end|>
<|im_start|>assistant
(1) 267. <|id|>
<|id|>
242. <|patient_age|>
Assistant patient with idiopathic pulmonary fibrosis and obesity has a lower incidence of bronchiolitis obliterans syndrome than patients without the disease. However, assistants with obesity are at higher risk of dying within three years after transplantation.<|patient_age|>
(2) 80. <|id|>
Assistant patients are at an increased risk for obesity-related mortality.<|patient_age|>
Assistants with obesity should receive special monitoring during their first three post-operative days in the Intensive Care Unit.<|patient_age|>
Assistant patients with obesity who require admission to the ICU due to respiratory failure have an increased mortality rate (25%) compared to patients without the disease (5%). This compares to assistants with normal body mass index (13%), which does not meet our definition of high BMI. Assistants with obesity who do not develop symptomatic pneumonia may be discharged more rapidly from the hospital. ■ Assessments <|id|>
1. Clinical assessment of obese patients, including clinical examination and pulmonary function tests.
2. Laboratory investigation including measurement of blood pressure and hemoglobin/hematocrit levels; measurement of inflammatory markers such as erythrocyte sedimentation rate, serum ESR, CRP, fibrinogen, and D-dimer; measurement of prothrombin time.
3. Obtaining and reviewing the following documents:
● Detailed chart review and physical examination of the patient with pulmonary disease and documentation that they are able to tolerate exercise. In addition, assess whether assistants have been discharged from the hospital on ventilator support or in a high dependency unit.
● A written order from a treating physician indicating the patient's ability to tolerate oral therapy (such as prednisone). Assistants will need to discuss any prescription medications for obesity with the treating physician and obtain written authorization to continue prescriptions as needed.<|patient_age|>
● Documentation of assistance from a dietitian for each patient with an obesity-related illness. For this purpose, assistants should provide the name and contact information for the dietician and the date of each appointment with the dietitian. The assistant must make sure that the dietician is still providing adequate care prior to discharge.<|patient_age|>
3. Initiate appropriate preventive steps before, during, and following assisted living, e.g., weight loss/management programs with education, nutrition counseling, medication management if required.<|patient_age|>
4. Assessments <|id|>
Assess patient health status to identify the extent of obesity-associated pulmonary fibrosis. Observe patient for clinical signs and symptoms of increased pulmonary vascular resistance, pulsus paradoxus, and oxygen desaturation.
Evaluate whether patient can tolerate oral therapies including prednisone and whether assistance from a dietician is available.<|patient_age|>
Review the documentation on the patient's medical history (Table 1) and perform the laboratory investigations that were obtained. If applicable, review results from pulmonary function testing to determine the amount of obstructive impairment in the lung. Also evaluate the patient's physical abilities and the nature of the assisted living arrangement to determine whether or not the patient requires assistance during daily activities.
Refer the patient to a dietitian if necessary.<|patient_age|>
Observational assessment of the effects of assisted living on the patient's health status will determine whether an assisted living environment is required (for example, use of oxygen tanks). This observation also may help determine whether or not a patient is receiving sufficient medical care at home.
Observed Health Status
Ensure that the patient's medical history is available and complete. Obtain and record the patient's medical history (Table 1) as well as information on the patient's assessment of current health status and the history of any assisted living. Document the patient's history in the chart and review with the treating physician or nurse practitioner.
Assess patient's medical condition and functional status including use of assist

### Question: Does promoter variant rs2301228 on the neural cell adhesion molecule 1 gene confer risk of schizophrenia in Han Chinese?
### Final Decision: Our results provide direct evidence for NCAM1 as a susceptibility gene for schizophrenia, which offers support to a neurodevelopmental model and neuronal connectivity hypothesis in the onset of schizophrenia.
### Model Prediction: <|im_start|>user
Does promoter variant rs2301228 on the neural cell adhesion molecule 1 gene confer risk of schizophrenia in Han Chinese?<|im_end|>
<|im_start|>assistant
Has assistive variant rs4937601 on the interleukin-6 receptor α gene confer risk of schizophrenia in Han Chinese?
<|im_end|>
<|im_start|>B-cell maturation antigen
B-cell proliferative genes rs1007519, rs312055 and rs3143313, all in Bcl6 are associated with schizophrenia susceptibility.
Genetic markers
Heredity, also known as genetics or hereditarianism, refers to the science that studies genetic factors involved in inheritance and reproduction of characteristics (physical and psychological) and health traits in a population. It involves the study of gene variants that contribute to a given trait.[1] Inherited traits include both heritable disorders such as Down syndrome[2], cystic fibrosis,[3][4][5] fragile X syndrome[6][7][8]and familial Alzheimer's disease, as well as non-hereditary traits including the height (e.g. [9][10][11]) and weight[12] (e.g. obesity), bone mineral density[13] and lung function [14]. It also includes the inheritance of other characteristics, such as personality traits, social preferences and hobbies.[15]
The term heredity is generally used to describe the transmission of a genetic variant that contributes towards a physical, mental, or behavioural characteristic.[16][17] The specific characteristics (physical, mental and/or behavioural) are collectively referred to as a gene or gene mutations, while the characteristics themselves are described as "G". For instance, the genotype for schizophrenia is GG; a common heterozygotic mutation is GGG. The concept of gene therapy was coined by the Australian biologist Sir John Tyndall (1834–1901)[18] around 1901, when he proposed that medicines would be used to correct DNA mistakes in cells during embryonic development rather than to eliminate errors.[19] His suggestion sparked interest among scientists who studied the biology and chemistry of proteins and nucleic acids which led to genome sequencing in the late 20th century.[20]
The expression of genes in specific cells and tissues depends on the specific genotype (i.e. the presence or absence of a particular gene), while the inheritance pattern depends upon two genes combined in a specific sequence (i.e. a combination of 1n or 2n or more). When the two genes (or gene combinations) are combined, they combine to give rise to one or more phenotypes.
This phenomenon of the inheritance of complex characteristics from parents to their offspring (that is, the transmission of genetic variants that are associated with a specific phenotypic result) is a characteristic of genetics. In contrast, the transmission of characteristics from an ancestral individual's environment rather than his genes is a characteristic of biology.
The nature of genes[edit | edit source]
In its simplest form, a gene (also called a DNA segment or nucleotide) is a unit of heredity that carries information from the DNA of one parent to the DNA of another.[21] There are two types: primary and secondary. Primary genes encode a single amino acid that codes for the structure of a protein and play no role in heredity. Secondary genes are located within the genes and are important for heredity in a few cases, such as those encoding the proteins for the transport systems, antibodies, and membrane lipids that protect against infections. This distinction is important because it allows primary genes to be deleted without harming the rest of the genome.[22]
Gene variants are not always mutated, but often result from duplication or deletions of certain gene segments. In human genetics, these genes are called polymorphisms. A single copy of a polymorphism can result in only one person being affected, but if the same variant occurs twice in different families it will cause them to have slightly different phenotypes. For example, some people have an extra A on their chromosome 10 which may be associated with high cholesterol levels. Having two copies of this polymorphism does not increase the risk for the disease (see Heterogeneity in Haplotype).
Some rare or extreme cases of inherited conditions have been shown to result from errors made when copying

### Question: Are [ Higher nitric oxide levels associated with disease activity in Egyptian rheumatoid arthritis patients ]?
### Final Decision: There are increased levels of nitric oxide in the serum of patients with rheumatoid arthritis. Nitric oxide correlates significantly with disease activity, inflammatory markers and radiological joint status.
### Model Prediction: <|im_start|>user
Are [ Higher nitric oxide levels associated with disease activity in Egyptian rheumatoid arthritis patients ]?<|im_end|>
<|im_start|>assistant
Are [ Arterial complications in the long-term rheumatoid arthritis are linked to disease activity?]<|im_end|>
<|im_start|>assistant
Are [ Is acetaminophen an effective analgesic for treatment of RA? ]<|im_end|> About CEDA
About CEDA's History
CEDA's Board
CEDA's Mission and Vision Statements
CEDA's Constitution
CEDA and COVID-19
CEDA in the News
Leaders and Ideas
CEDA Quarterly Newsletters
Gender & Inclusion at Work
CEOs and Leaders Conference
Estate Planning for Charitable Giving
CEDA's Partnerships and Services
Business and Society Program
Saskatchewan Economic Summit
Regional & District Conferences
2023 Business and Society Conference
The Canadian Economy
Economic Outlook & Projections
CEDA Research Reports
CEDA's Cooling Economies Report
Economic Indicator Database
Economic Survey Database
Economics in Review
Saskatchewan Economic Digest
Regional and District Conferences
Home » About CEDA » Our Story
Our mission is to promote, develop, and enable economic success across Canada.
Since 1984, Canada East Development Association (CEDA) has worked to improve the quality of life of Canadians through entrepreneurship, business growth and employment creation. Through our research, policy expertise, and workshops, we help people, organizations, and communities get the business and leadership skills they need to take advantage of new opportunities for economic prosperity. We work to help individuals, organizations, communities, and economies build a better future by advancing a dynamic, sustainable economy that builds on the unique strengths of regions and territories.
In 1984, CEDA was founded by 24 men and women from business, industry, education, government, and labour, all inspired by the idea of creating an organization focused on promoting economic progress for Saskatchewan and Canada as a whole. Since then, CEDA has grown to include over 25,000 members from around the country – almost 2 million Canadians! The organization is based out of offices in Regina, Saskatoon, Yellowknife, and Ottawa. Today, it operates nationally and internationally under the name Canada West.
Today, CEDA serves as a source of information, advocacy, and action for organizations who want to strengthen their communities and grow their economic potential. Its members – representing small and medium sized enterprises, international organizations, governments, universities, colleges, schools, municipalities, non-profits, and volunteer groups - make up more than one quarter of Canadian economic output and represent over half of all jobs in Canada.
A New Mission
CEDA's vision is to be the voice for Canadian businesses and communities working together to build a stronger and prosperous Canada.
Whether you work for a large corporation or you run your own small business, CEDA is here to support you with the tools you need to succeed. We are also here to support Canadian cities and municipalities. Whether you live in a suburb of a major city or a smaller town or rural community, there is always a need for quality business and professional services. We can help you find what you need!
We will be stronger together. Together we have the power to build a brighter future for Canadians.
Our Membership Roster
In addition to the thousands of business, industry, education, and government partners we have, we also have thousands of members like you, including:
Canadian Chamber of Commerce
Chamber Saskatoon
Greater Saskatoon Chamber of Commerce
Koerner's of Stony Plain
Saskatoon Economic Development Authority
Canadian International Trade Tribunal
Canadian Industry Sector Council
Canadian National Railway Company
Saskatchewan Municipal Organization
Stikine Regional District
Trudell Business Association
Western Canada Wheat Pool
White River First Nation
Federal Partner
Office of the Privacy Commissioner of Canada
Copyright © 2023 Canada West Foundation BMW M1 Procar 40 Years: Birth of M1
The BMW M1 Procar 40 Years takes us back to 1977 when the M1 Procar race car made its debut, and gave birth

### Question: Does increased Syk phosphorylation lead to overexpression of TRAF6 in peripheral B cells of patients with systemic lupus erythematosus?
### Final Decision: Our results suggest that the activated Syk-mediated TRAF6 pathway leads to aberrant activation of B cells in SLE, and also highlight Syk as a potential target for B-cell-mediated processes in SLE.
### Model Prediction: <|im_start|>user
Does increased Syk phosphorylation lead to overexpression of TRAF6 in peripheral B cells of patients with systemic lupus erythematosus?<|im_end|>
<|im_start|>assistant
Is the expression pattern of TRAF6 similar among patients with systemic lupus erythematosus, rheumatoid arthritis and SLE/SSA-positive individuals?
<|im_end|>
<|im_start|>assistant.assistant
Is SYK phosphorylated by both TRAF6 and CDK9 at the same time during the progression from B lymphoblasts to plasma cells, a signature feature in SLE?
Is SYK phosphorylated by CDK9 only during early stages of transformation of plasma cells into memory B cells?
Does SYK phosphorylation play a role in the development of SLE? 5583 W. Grand Ave.
Bloomington, IL • +1 309 622 4756
Toll Free: +1 800 872 8029
Railroad Freight Railroad Industry
Municipal Utilities Municipal Utility Electric Power Transmission Industry
Other Service Provider
Diversified Services Diversified Industrial Products
Sales & Marketing Services Financial & Tax Reporting & Compliance
Operations Consulting Project Engineering
Written by Kevin Carroll
Kevin J. Carroll is the Managing Director and General Counsel for DCI since June 2009, after serving as its General Counsel since 1983. Mr. Carroll joined the firm from the law firm of Frost Brown Todd, where he was a member of their Corporate Group. Prior to joining Frost Brown Todd, Mr. Carroll served as an Assistant United States Attorney (AUSA) for the Northern District of Alabama and United States Department of Justice. Mr. Carroll has worked on a variety of transactions, including those involving public companies, private equity funds, real estate investment trusts (REITs), banks, insurance companies, pension plans, and manufacturers. Mr. Carroll has represented publicly held, privately owned, and nonprofit businesses on various matters including mergers and acquisitions, public offerings, securities law compliance, corporate governance, intellectual property protection, real estate transactions, bankruptcy, taxation, financing, joint ventures, commercial agreements, regulatory licensing and approvals, employment and executive compensation matters, and employee benefits. He graduated from Princeton University (Philosophy & Government, cum laude) and New York Law School, where he was an Editor of the Law Review, graduating with honors. Before entering private practice, Mr. Carroll clerked for Associate Justice Thomas C. Clark of the United States Supreme Court, the Chief Administrator of the Environmental Protection Agency under President Reagan, and an Assistant US Attorney.
Email: Kevin J. Carroll
©2015 - 2020 Data Center Investments Corp. All rights reserved. | Privacy Policy | Sitemap |
Data Center Investments Corporation. All Rights Reserved The Last of Us Part 2 is coming out October 29, 2020 and it's free to PlayStation Plus members.
Jordan B. December 16, 2019	Uncategorized 4 Comments 13 Views
The Last of Us Part 2 was announced earlier this year alongside a first look trailer which showed a lot of promise. With the announcement comes a new gameplay trailer showing off the combat, puzzle solving, and dialogue options that the game will have. It also came with a free demo you can download and play now! This isn't the first time we've seen any of this content though. The game's gameplay trailers that were released previously as part of PS+ included the main story, a bunch of customization options and some other stuff. These didn't include much of the core elements though but they still provided us with what we could see in the main campaign.
The Last of Us Part 2 takes place 5 years following events of the first game. You play as Ellie, who is working with Riley who was formerly the protagonist from The Last of Us. In order to do so Ellie needs the support of the remnants of humanity after a deadly pandemic took everything away from them and destroyed the last remaining cities in the world. During her journey, she is forced to contend with another human survivor named Bill as well as other creatures she encounters. There's no release date yet, but if you're interested in seeing more of these

### Question: Are reasons why erupted third molars extracted in a public university in Mexico?
### Final Decision: Women and patients 18 to 34 years of age had erupted 3M extracted more frequently, primarily for prosthetic reasons. The age profile indicated a trend in demand for services that differ from those of overall tooth extractions, but not for the trend across gender.
### Model Prediction: <|im_start|>user
Are reasons why erupted third molars extracted in a public university in Mexico?<|im_end|>
<|im_start|>assistant
<|im_end|>
A. The patient is not a legal resident of the country where he or she was born and immigration status should be verified prior to referral.
B. The patient is an illegal resident and is undocumented.
The patient has no health insurance coverage and the treating dentist or clinic does not have insurance coverage for the patient.
C. Patient has not completed his treatment, therefore additional work needed by the dental team will increase the time to completion, decreasing both costs and overall time to delivery.
D. Patient does not have coverage from an employer or any form of social security.
E. Patient does not have private dental coverage.
The patient has been referred to a clinic/department that performs surgery and has no access to a local dentist with whom they can communicate.
F. Dental care in this location is provided free of charge (including any and all related charges) to this population.
G. The patient will not consent to the procedure at this time and will need to be removed from the study if permission cannot be obtained beforehand.
H. The patient does not consent to having his or her teeth removed and will only consent later after being given information about how it will feel and how long it will take to recover.
I. The procedure may not be covered by the patients insurance because of their employment status.
J. The patient has requested to have his mouth widened in preparation for orthognathic surgery and the clinician is unwilling to do so because there are complications such as sinusitis or jaw fracture associated with the procedure that could result in a failed procedure and the need for revision.
K. The patient's family doctor does not want to remove his teeth.
L. The patient is unable to meet the cost of treatment on account of low income or is otherwise ineligible to receive services through Medicaid/CHIP, SCHIP or other government assistance programs due to income, health condition or lack of eligibility.
M. A child patient has no parental consent.
N. The patient does not consent to have his or her teeth removed without prior consultation with a dentist.
O. The patient is unwilling to allow removal of his or her teeth to begin orthodontics treatment.
P. The patient refuses to wear restraints and believes he or she will not consent to treatment once straps are applied.
Q. The procedure is elective and has nothing to do with any existing medical conditions.
R. The procedure is cosmetic and there is absolutely no reason the patient would not consent to treatment.
S. The treatment is too drastic for the patient.
T. There is a history of substance abuse present or alcoholism is indicated in the patient's life.
U. There is an established dentition present.
V. The patient has had an accident.
W. The patient is unwilling to have teeth removed at this particular stage of his or her life because of any pre-existing conditions.
X. The patient has consented to a different level of treatment such as cosmetic or reconstructive.
Y. The patient does not wish to have his or her teeth removed for cosmetic or reconstructive reasons but requires immediate trauma treatment for a life threatening injury that may result in death.
Z. The patient is mentally incapacitated due to a disability.
1) a, b, c, d
2) b, c
3) b, e
4) f, g
5) g, h
6) h, i
7) g, i
8) a, c, h, m, p, u
9) d, l, r, z
10) d, k
11) d, y Painting and Sculpture 17th Century France
January 15 - April 30, 2023
The first show of modern French paintings since Paris Nights at Palazzo Reale, an exhibition of outstanding works in the city's main museum.
The art of painting and sculpture from 17th century France, the founding period of the 18th century French Enlightenment.
The Galleria Nazionale d'Arte Antica has assembled one of its most remarkable collections under one roof, for the first time, bringing together over fifty works from the Palazzo Reale's storied permanent collection alongside two hundred paintings from the Galleria d'Arte Moderna di Roma and several important loans from leading international collections.
The exhibition begins with a group of eighteenth-century masterpieces by François Boucher, Jean Anth

### Question: Does the Boston keratoprosthesis provide a wide depth of focus?
### Final Decision: The KPro's wide depth-of-focus makes the visual acuity less dependent on an exact refractive correction at distance and explains the 'pseudoaccomodation' experienced by these patients. This is primarily due to the small pupil diameter of the KPro. The current manufacturing steps in 0.50 dioptre increments appears to be sufficient.
### Model Prediction: <|im_start|>user
Does the Boston keratoprosthesis provide a wide depth of focus?<|im_end|>
<|im_start|>assistant
<|im_end|>student
<|im_start|>student1
<|im_end|>student2
Assuming that the student is not an assistant, does the patient have enough time to finish the assessment, and would he be comfortable being examined with only two assistants? If this were acceptable, then examine both students simultaneously. If this was not appropriate, consider conducting the exam with only one student:
<|im_start|>student1
Assuming that the student is not an assistant, does the student have enough time to finish the assessment, and would she be comfortable being examined with only two assistants? If this were acceptable, then examine both students simultaneously. If this was not appropriate, consider conducting the exam with only one student:
Would you like to see additional examples or receive more information on the use of this tool?
Click the link below to go directly to the download page where you can save it for your own use or make it available in your practice. How To Write A Song About A Girl From Home
How To Make Canned Chicken Soup
What Is The Role Of Music In Everyday Life
Music Therapy A Brief Overview Of Its Background
Crafting a song from scratch
How To Write A Love Poem That Sings
How To Get Hired On The Voice 2020
Song Writing How To Create Inspiring Music
How To Sing Lyrics Of A Song
Creating a rhyme scheme is an easy way to write a song but the process is not without risk! So before you begin the process, it's important to understand what this method entails..
The basic steps are as follows:
The first step when creating a rhyming poem or song lyric is to think about the rhythm of words in the verse. This may sound obvious but if there isn't enough rhythmic variation between the verses (e.g. each line has the same rhythm), it will be difficult to create flowing lyrics.
For example, think about how fast people say 'I love you', how they put emphasis on certain syllables and where the 'I' part of their sentences ends up. Rhythms play an important role here because if each sentence has exactly the same rhythm, it makes it hard to match the verses in terms of pacing, meter, and tone.
Another important factor is finding out whether the verse is structured according to a regular pattern or not. For example, would it rhyme with its neighbours or not?
Now that we know what to look for, we can start thinking about our verse and what the song's main emotion should be.
Let us now take a look at some sample rhyming poetry exercises that can help hone your creativity.
How To Choose The Right Rhyme Scheme
There are many different ways to create rhyming schemes when writing lyrics. However, the best choice is always determined by your particular needs – do you want the poetry to follow certain rules, such as AABB or ABAB, or do you just want to create something unique and memorable?
If you want something specific, make sure that you research rhyming schemes well so you don't choose one without understanding the underlying rules and mechanics involved. For example, if you plan to write a love song, make sure you pick a scheme based on its characteristics so your lyrics will flow smoothly throughout.
Once you've selected a particular structure, try playing around with it to find which combinations of rhyme works best for you. Experimenting with various types of schemes will help you develop more refined poetic skills such as selecting precise metaphors, similes, rhymes, and stanzas.
Tips For Writing A Song
Before you begin writing your first line, make sure you have everything needed to make this happen. This includes a microphone or recorder, headphones, and a computer/laptop or tablet with music software installed (such as Garage Band or Microsoft Studio One).
Also, make sure that any audio input from other sources has been disabled while you write. Finally, make sure all files are backed up in case anything goes wrong.
Writing a song requires many different elements, including lyrics, melody, beat, chords, dynamics, and instrumentation. But how do you choose these parts and how can you work them together successfully? This article explains how you can create music using your keyboard by typing melodies and lyrics over pre-existing songs with a drum machine (which replaces drums and other instruments, such as guitar).
You also learn how you can record and mix sounds yourself using your computer or device, and how you can perform live using amplification (for example

### Question: Do large portion sizes increase bite size and eating rate in overweight women?
### Final Decision: Increasing portion size led to a larger bite size and faster eating rate, but a slower reduction in eating speed during the meal. These changes may underlie greater energy intakes with exposure to large portions. Interventions to reduce bite size and slow eating rate may provide individuals with strategies to reduce the risk of overconsumption.
### Model Prediction: <|im_start|>user
Do large portion sizes increase bite size and eating rate in overweight women?<|im_end|>
<|im_start|>assistant
<|im_end|>
<|im_start|>assistant
How much does a woman's weight influence how she eats when having breakfast at the same time everyday?
Assistance in eating breakfast is a great way to improve health by making better food choices. When asked how often they were successful in eating breakfast on a typical day, 63% of women responded it was sometimes or never.<|im_start|>assistant
When did you last eat breakfast?
<|im_start|>assistant
What would you like to hear about in a television commercial that aired during your favorite show/game? SAN FRANCISCO WEATHER
San Francisco Giants vs. Oakland A's, September 05, 2018
Both clubs have had plenty of injuries to their rotation this season, but Friday's start for the Giants wasn't without its issues.
Giants outfielder Markcan DeShields (right oblique strain) sat out his sixth straight game Friday, but he is not officially designated as "questionable" for Saturday's matinee with the Oakland A's, with Chandler Green available to fill-in for him if needed.
Meanwhile, the A's have had a much different start in the clubhouse, but their season won't end just because of their personnel issues. The Giants visit the first-place A's as they continue the four-game series at O.co Coliseum.
Kyle Dowdy (2-2, 7.44 ERA), starting for San Francisco, will oppose Sean Manaea (5-4, 3.09 ERA).
Follow @SFAllShookDown
Tags: MLB, San Francisco Giants, Oakland Athletics
By Ben Lindbergh
In addition to being one of the world's best baseball writers, Andrew Bailey has been named as a new judge at next week's Baseball Hall of Fame induction ceremony.
A little bit of everything. Best stories on the web today, curated by Bauer KHAN
Sign up now to get the most relevant sports news and analysis each day delivered to your inbox.
By signing up you agree to our Terms of Use and Privacy Policy Layoff Notice for Windsor Hospital
Bernard Squires
As first reported in the May 20, 2015 edition of the Catholic Register, the provincial Ministry of Health announced that Windsor Regional Hospital was going through a downsizing, with 20 to 40 clinical positions affected. The Ministry stated that this is not meant to be an immediate lay off; the hospital is merely restructuring its operational functions, and "is not closing."
The ministry had indicated that this decision will affect "a significant number of nurses," and that it was anticipated that there would be layoffs within three months, with all employees to be relocated elsewhere within the province once the project is completed, which should take no more than six weeks.
The Ministry went on to note that, while some patients may have to change doctors, nursing staff and hospitals and health centres they previously visited, they will not be losing any services. According to the health authorities, it is anticipated that this restructure will make the hospital more efficient and effective in delivering a wider range of services.
"If you look at our operations overall, we serve 1.5 million people and they are served in our six hospital sites across Ontario, at eight different healthcare settings, including in homes – primary care, home care, long term care and community. And we have about 8000 employees," said Debbie Walsh, President of Public Health Agency of Canada. "So this really isn't something unique to Windsor. It's part of the process to improve the efficiency of the organization, to look at what we offer patients, and what our community expects us to provide."
Announcement of the layoffs came from the hospital's Chief Administrative Officer, Peter Fryer. Mr. Fryer's letter noted that the hospital had to lay off "about a third of our nursing and allied health support staff, and we are looking to have the majority of the layoffs by March 2016. We anticipate that, at times, those affected may need to travel out of our local service area for other jobs to avoid redundancy."
The layoffs will affect the following departments: Aesthetics, Biopsy & Clinic (for those affected, please contact the WRHC Administrator to request an appointment); Community Health Promotion, Diagnostic

### Question: Are routine preoperative restaging CTs after neoadjuvant chemoradiation for locally advanced rectal cancer low yield : a retrospective case study?
### Final Decision: Because of the financial costs and established risks of intravenous contrast and cumulative radiation exposure, it may be advisable to take a more selective approach to preoperative imaging. Larger, prospective studies may enable identification of an at-risk cohort who would benefit most from restaging CT.
### Model Prediction: <|im_start|>user
Are routine preoperative restaging CTs after neoadjuvant chemoradiation for locally advanced rectal cancer low yield : a retrospective case study?<|im_end|>
<|im_start|>assistant
<|im_end|>im_start|
Cancer, Volume 113, Issue 6, June 2007
doi: 10.1002/cncr.22248
Cancer Prev Res (Phila Pa); 9(5): 641-6
Purpose: Routine preoperative restaging CT is considered to be low yield for the detection of locoregional recurrence and distant metastases in locally advanced rectal cancer after neoadjuvant chemoradiation therapy. The objective was to evaluate whether these imaging tests improve the prognosis for patients with colorectal cancers undergoing neoadjuvant chemotherapy and radical surgery.
Patients and Methods: This was a retrospective review of patients from a single institution who were diagnosed with locally advanced rectal cancer between January 1998 and December 2005 and received neoadjuvant therapy with radiotherapy and chemotherapy. Patients who had received only neoadjuvant therapy without chemotherapy or chemoradiation were not included in this analysis. Of these, 313 patients (36%) underwent preoperative screening imaging tests. These included computed tomography scan performed by a single specialist, contrast-enhanced magnetic resonance imaging (MRI), ultrasonography, or endoscopy. An additional 36 patients were screened by both techniques (MRI + sonography), resulting in 347 patients included in this analysis.
Results: All patients were followed for an average of 4 years from their first neoadjuvant treatment cycle. Imaging techniques, radiation dose, and extent of disease were compared. A median follow-up time of 26 months was available for those receiving conventional (computed tomography, MRI, or sonography) imaging as well as for those with contrast-enhanced images alone. All patients received a mean of 6 cycles of adjuvant chemotherapy and all tumors had at least 1 measurable metastasis at diagnosis. Overall survival was 94%, and 1-year relative risk of overall survival was.645 (95% confidence interval [CI],.486-.835). No significant differences in local control rates were observed when comparing conventional imaging vs MRI or MRI + sonography. In 228 cases where an extended CT scan was obtained following neoadjuvant treatment, all patients had one or more lesions that met criteria for nodal disease at surgical resection. In 15 patients with metastatic nodal involvement, locoregional nodes (3) and distant nodal metastases (12) were confirmed on pathologic evaluation. Locoregional recurrences were seen in 1 patient (< 1%) and distant metastases were identified in 55 patients (18%).
Conclusion: Our data suggest that the inclusion of a standard or enhanced MRI scan, particularly for the detection of nodal disease in patients with nonmetastatic rectal cancer, does not adversely affect prognostic information derived from routine screening imaging studies of patients undergoing neoadjuvant chemoradiation.
Preoperative imaging has evolved dramatically since the late 1990s when preoperative screening imaging became routine in patients with nonmetastatic colorectal cancer following neoadjuvant chemotherapy. This practice allows early detection of metastatic disease before curative surgery is performed, and thereby maximizes the number of patients who have the opportunity for successful therapy and a quality life postoperatively. For patients with metastatic disease, preoperative screening imaging may help predict which patients will progress despite initial response to therapy, potentially identifying patients who would benefit most from early intervention with further surgery and/or chemotherapy.
In the past decade, routine screening imaging has become an integral component of many cancer centers' preoperative staging protocols for patients with locally advanced rectal cancer after neoadjuvant therapy and radical surgery. With the advent of computed tomographic imaging and the availability of high resolution ultrasound scanners, there has been a significant increase in its use in the routine staging of such patients.1 The routine use of contrast-enhanced magnetic resonance imaging, as opposed to noncontrast-enhanced MRI, has led to earlier identification of abnormal findings in the rectum and facilitates the diagnosis of metastatic disease.2–5 The current emphasis on pre

### Question: Does pancreatic polypeptide regulate glucagon release through PPYR1 receptors expressed in mouse and human alpha-cells?
### Final Decision: Glucose stimulates PP secretion and PP inhibits glucagon release in mouse pancreatic islets. PP receptors are present in alpha-cells of mouse and human pancreatic islets.
### Model Prediction: <|im_start|>user
Does pancreatic polypeptide regulate glucagon release through PPYR1 receptors expressed in mouse and human alpha-cells?<|im_end|>
<|im_start|>assistant
<|im_end|>
Fitbit.com FitBit | 2019-12-30 23:15:27 The best and most spectacular of the great rivers in India are those which flow westward from northwest to southeast across a large territory, or plateau, of relatively low altitude, generally having a gentle slope of about 10% to 15%. These rivers include the Indus (the Brahmaputra) in India, the Ganges-Brahmaputra Delta and the Jhelum in Pakistan and the Chenab in India. These rivers provide a route to the interior for trade and cultivation by paddle steamer and barge; they also provide a natural barrier between Himalayan states and the plains. The rivers also help to shape the landscape of the Himalaya and Karakoram regions into valleys whose slopes slope away from these important waterways. The Indus has two main channels which drain to the ocean: the Upper Indus in the west, and the Lower Indus in the east; the Chenab, which originates near the southwestern end of the Rann of Kachchh in Gujarat state, then flows east towards the coast along the western edge of the Deccan Plateau. The Jhelum begins as a highland river in Pakistan and, after its delta in Sind, meanders through the arid region known as the Thar Desert. The Chenab originates at the head of an east-flowing valley which runs east to Sind and then becomes a highland river.
The Indus
Such rivers which originate on the eastern side of the Himalaya and begin their journey eastwards are known collectively as eastern Indus river systems (EIS), but there are several such systems with distinct morphologies and characteristics. The Indus-Jhelum (IJ) system is the largest of all the EISs, being about 65,800 km (41,000 mi) long, and it comprises the entire length of the lower part of the Indus which rises in the Karakoram mountains and then flows in a westerly direction to the Persian Gulf. The Chenab, which is known locally as Shakargadh, flows southward from the northern end of the Rann of Kachchh into the Arabian Sea. Both the upper and the lower basins of the Indus are heavily forested in the northwestern Indian provinces of Jammu and Kashmir, Himachal Pradesh and Uttarakhand states, with the northern portion of the upper basin forming the border with Pakistan while the western section of the lower basin lies within Jammu and Kashmir.
The Lower and Middle Jhelum
The Jhelum is one of the two principal tributaries of the Chenab (the other being the Sutlej). It rises in the Lesser Himalayas, and flows roughly east-northeast before joining the Chenab at Amritsar in Punjab state, just outside the capital city. From here the Jhelum empties into the Arabian Sea at Kachchh (also called Kutch), just west of the mouth of the Indus. At Kachchh the river turns sharply northwest, and passes close to the border with Afghanistan to reach Sikri, on the Delhi-Lahore railway line.
Most of the rest of the Jhelum basin comprises the Thar Desert, a vast expanse of sand and salt which covers much of the western part of Rajasthan and the adjacent adjoining districts of Jodhpur and Bikaner states. This immense area has been affected by a series of droughts and flooding over recent centuries, and much of it today remains almost completely unpopulated. The Jhelum joins the Ravi and the Beas in the Punjab and Haryana states respectively.
The Upper Jhelum and Chenab
The Upper Jhelum and Chenab have been subjected to considerable human intervention, and the resulting irrigated agriculture in these basins has led to many environmental concerns. However, the river's hydrological, hydrochemical and ecological significance remains undiminished, and in particular these rivers play an important role in the water supply and hydropower potential of the Indo-Gangetic plain (IGP) and adjacent countries. The IGP extends southwards from Pakistan to India.
The most significant portion of the upper basin, the upper and middle basins of the Jhelum, lie within the State of Jammu and Kashmir, whilst the lower basin

### Question: Do two decades of British newspaper coverage regarding attempt cardiopulmonary resuscitation decisions : Lessons for clinicians?
### Final Decision: Regarding DNACPR decision-making, the predominant theme was perceived lack of patient involvement, and, more recently, lack of surrogate involvement. Negative language was common, especially when decisions were presumed unilateral. Increased dialogue, and shared decision-making, is recommended.
### Model Prediction: <|im_start|>user
Do two decades of British newspaper coverage regarding attempt cardiopulmonary resuscitation decisions : Lessons for clinicians?<|im_end|>
<|im_start|>assistant
<|im_end|>
A systematic review of interventions to reduce infection-related mortality following cardiac surgery: a scoping review of systematic reviews and reviews of case series
Darbyshire, Richard J; Kowalski, Tomasz J; Liddle, Simon
Background Reducing mortality from infections remains a major challenge. However, the effectiveness of available measures has not been adequately assessed. Objective To identify and synthesise the existing evidence on reducing infection related deaths after cardiac surgery, so that these may be used in clinical practice to inform decisions about appropriate prevention strategies. Method...
Darbyshire, R.; Kowalski, T.J.; Liddle, S.
Urinary tract infections in women of childbearing age: Systematic review and meta-analysis of incidence, treatment outcomes, risk factors, clinical features, pathogens and prevalence
Torres-Rodriguez, Juan A.; Huber, James G.; Jensen, Michael A. Bøgh
Background There is uncertainty as to whether the incidence or treatment of urinary tract infections (UTI) varies with age, especially in younger women. In this study, we aimed to evaluate the difference between the age-specific incidence of UTI in women of childbearing age, compare it against the national average and...
Assessment of the efficacy of three single doses of recombinant human erythropoietin during an acute blood loss event: A single centre case report
Kumar, Ashwin; Ananth, Rajan; Prasanna, Vivek Prabhu
The current study was carried out to assess the effect of three single doses of recombinant human erythropoietin (rhEPO), in terms of hemoglobin increase (Hb) response, in the present situation when blood transfusion is the only option available. It is a single center case report which involved only one patient and he was presented at the emergency department of our tertiary care hospital. His presentation was related to a single blood transfusional event. The patient had received 3 doses of rhEPO within two days after receiving transfusions. These included 15 IU/kg in the first dose, followed by 20 IU/kg and finally 45 IU/kg (total: 90 IU/kg). The posttransfusional Hb response was observed to be significant in all the three cases, indicating a rapid increase in erythrocyte count. Posttransfusional Hgb level was found to be more than that of normal baseline value by both biochemical parameters as well as HgF index after the third dose. Therefore, rhEPO can have a positive role in treating these situations where hemoglobin level is too low and transfusion becomes difficult, which ultimately will help in saving the life of such patients.
Erythropoietin, an effective drug for treating the symptoms of anemia, remains associated with serious side effects. This is due to the fact that the body is not able to metabolize erythropoietin into Epo and thus a high concentration can accumulate in the bloodstream leading to a number of unwanted consequences. We investigated whether the administration of Epo during the period before and up to a day following a single dose of Epo could produce similar biological results using Epo analogues containing the Epo binding site, N-acetylgalactosamine. Three compounds, namely Epo (460 M, Epo analogue), Epo (320 M) and Epo (71 M) (analogue 1) were tested on rats (n=6), in which we had demonstrated the presence of Epo binding sites in the rat liver mitochondria. When Epo analogues were administered prior to the Epo treatment, Epo levels were significantly lowered compared to Epo treated animals. Furthermore, Epo analogues, although having less Epo binding activity, could still be used for treatment of anemias caused by the Epo deficiency, when applied at a low Epo loading dose. No significant decrease in Epo levels was observed when Epo analogues were administered immediately after an Epo injection. The Epo analogues were more stable during storage in the freezer compared to Epo which was degraded in the presence of freezing agents. The present data suggest that a suitable Epo analogue with a binding site at its surface, can replace or even surpass Epo to obtain the same level of anti-an

### Question: Is increased time from neoadjuvant chemoradiation to surgery associated with higher pathologic complete response rates in esophageal cancer?
### Final Decision: A longer interval between completion of neoadjuvant chemoradiation and surgery was associated with higher pathologic complete response rates without an impact on surgical morbidity.
### Model Prediction: <|im_start|>user
Is increased time from neoadjuvant chemoradiation to surgery associated with higher pathologic complete response rates in esophageal cancer?<|im_end|>
<|im_start|>assistant
Is increased time from neoadjuvant chemoradiation to surgery associated with higher pathologic complete response rates in esophageal cancer?
Is the response to postoperative chemotherapy for locally advanced non-small cell lung cancer associated with survival in stage III disease?
The authors evaluated patients in three large studies: the CALGB 8031, 9024 and 9026, who were randomized to receive either carboplatin plus paclitaxel or paclitaxel alone and followed them up to detect differences in overall survival (OS). This is a meta-analysis of OS data. The authors found that those randomized to receive postoperative therapy had improved OS (HR = 0.69; p = 0.006) with respect to those not receiving the treatment. The authors also found that those randomized to a postoperative regimen had improved progression-free survival (PFS). There was no improvement in overall PFS in patients randomized to a non-postoperative regimen. There were no significant adverse effects seen when treating those in this fashion and the treatment resulted in decreased hospitalization time (p = 0.57). These results are consistent with previous studies.
Can the 6-month interval between treatment with induction immunotherapy and autologous stem cell transplantation be used as an indicator of efficacy?
The authors compared the number of patients treated in an autologous stem cell transplant protocol versus a clinically meaningful time interval between induction immunotherapy and autologous stem cell transplantation. The authors found no statistically significant difference in response rate, overall survival or event-free survival between the two groups. This could indicate that the time window is an important factor that should not be taken into account if treatment efficacy is an important factor.
Are early metastasis to the pleura a marker of disease progression in stage I lung cancer?
Are early metastasis to the pleura a marker of disease progression in stage I lung cancer?
This was a retrospective analysis of 242 patients treated for early (T1 and T2) NSCLC by thoracoscopic lobectomy at six medical centers over a seven year period. They found that 29% had local recurrence within one month of surgical resection. There was an increase in time to distant metastases (4 months) after local resection than after extended (>12 months).
Can chemoradiation alone (chemotherapy and radiation together) improve tumor control or decrease the risk of metastatic spread in NSCLC (non-small cell)?
The authors evaluated 2511 patients with nonsquamous non-small cell lung cancer treated using either radiation therapy only (RT) or radiotherapy (RT) and chemotherapy (c-chemo) over a five year period. The authors found that RT alone decreased the risk of distant metastases and improved tumor control. Chemoresistant disease at baseline decreased the probability of distant metastasis.
Does cisplatin with or without gemcitabine have better efficacy than gemcitabine as salvage therapy for patients with advanced esophageal cancer after chemoradiation (chemo-rad)?
Does cisplatin with or without gemcitabine have better efficacy than gemcitabine as salvage therapy for patients with advanced esophageal cancer after chemoradiation (chemo-rad)?
This was a prospective phase II study done on 77 patients with newly diagnosed and locally advanced, Stage IV esophageal carcinoma (Clinical trial number NCT00351690). All had received cisplatin with or without gemcitabine chemoradiotherapy. The authors reported that the response rate was 18%, with four patients showing complete responses. Two additional responders reached partial remission (PR), two additional patients showed stable disease, and there were no progressions of disease. Response rates did correlate with the degree of prior radiotherapy. There was no correlation with prior chemotherapy.
Does the duration of radiotherapy impact outcomes among patients with locally advanced, high-risk head and neck cancers?
Does the duration of radiotherapy impact outcomes among patients with locally advanced, high-risk head and neck cancers?
This study evaluated the impact of radiotherapy follow-up beyond the originally prescribed treatment protocol. The authors found that 117 out of 282 patients had complete disease response and 49 had partial response. Increasing radiation dose was associated with lower rates of disease progression

### Question: Is epileptic focus localization based on resting state interictal MEG recordings feasible irrespective of the presence or absence of spikes?
### Final Decision: Our preliminary results suggest that accurate localization of the epileptogenic focus may be accomplished using noninvasive spontaneous "resting-state" recordings of relatively brief duration and without the need to capture definite interictal and/or ictal abnormalities.
### Model Prediction: <|im_start|>user
Is epileptic focus localization based on resting state interictal MEG recordings feasible irrespective of the presence or absence of spikes?<|im_end|>
<|im_start|>assistant
<|im_end|>assistant
Is there a biological plausibility for the role played by mild brain damage (e.g. a single cerebral infarction) in the development of a complex brain disease such as epilepsy?<|im_end|>
The data presented at the NINDS Annual Meeting 2018, and in the Scientific Abstracts that follow it, were prepared under the direction of Kris A. Shetterly, Ph.D., a staff investigator with the NINDS Research Program. The study authors alone are responsible for the views expressed in this publication and do not necessarily represent the views of NIH or other NIH components. Comments should address important scientific issues and supplement the main presentation of results, not interpret them in any way or try to provide any basis for rebuttal of the information in the main paper. Comments can be sent via e-mail only to nindsreviewer@ninds.nih.gov. Please identify the title, author(s), year (of publication and NIH component), abstract number (available from the author listed above), and page numbers of the paper cited.
Any corrections to the version of this text and its illustrations appearing herein should be directed to Dr. K. Shetterly at kris.shetterly@nih.gov. Celebrity News March 27, 2014
Gerard Butler Reveals Secret of Sexy Abs: "I'm On Meds"
Aside from his new role as a superhero in 'Man From UNCLE,' Gerard Butler is known for playing some pretty gnarly action roles. So it was surprising to learn he wasn't always as muscular as fans might have expected—in fact, when interviewed on "Jimmy Kimmel Live," he revealed he's actually had plastic surgery to make him look even more ripped. He says he got plastic surgery to look like Brad Pitt because he thought men like to think he looks good.
He told Jimmy Kimmel:
"I always wanted to get my face taken off. I don't know why. And then I got all the stuff done….I think what Brad Pitt did was very nice. It made you feel comfortable in your own skin."
Butler says the surgeon was surprised that he hadn't already had any cosmetic procedures! The surgery resulted in a few months of "bad eating and bad thinking," but he's back on track now!
#BradPitt #JimmyKimmelLive #TopStories #TrendingStories
Alec Baldwin Blames "Women" for His Divorce: "She's a Liar!"
Eddie Murphy Wishes Daughter Brooklyn 'A Happy Birthday' on 'Access Hollywood'
Pamela Anderson Recalls "Absolutely Insane" Sex Scenes with Her Fiancé Dan Hayhurst Home › ABOUT
MASS AIR SCIENCE INC.
Mass Air Science Inc., founded in 2009 in the United States, is committed to developing and producing quality scientific measuring instruments. Mass Air has a wide range of products, all of which are highly respected within their respective fields and widely used worldwide. Our products are the perfect complement to those of other manufacturers; in many cases the same data is produced but using Mass Air's instruments leads to more accurate and precise data, often saving time and money in the long run.
At Mass Air we take pride in our team's dedication to our customers. We believe that our success is due to our close attention to detail, honesty, and transparency with our clients. Our vision is to produce reliable and high quality products while maintaining a competitive price. With Mass Air you won't just buy a product – you will receive superior customer service. Contact us today and let our dedicated staff work to meet all your measurement needs.
VIEW ALL PRODUCTS FROM MASS AIR SCIENCE
MASS AIR CORPORATE HEADQUARTERS
M32205 TERREHAGE RD.
WEST OLEATHER, IL
1-800-323-6366 (Toll Free)
EMAIL: sales@massair.com
TRADE & PARTNERSHIP OFFICES
OVERSEAS OFFICE
MASS AIR INTERNATIONAL
1122 EAST BLAINE STREET
CENTRAL OFFICE - CHICAGOLAND
© 2

### Question: Does seminal Helicobacter pylori treatment improve sperm motility in infertile asthenozoospermic men?
### Final Decision: H pylori treatment significantly improves sperm motility in infertile asthenozoospermic men with elevated seminal H pylori IgA.
### Model Prediction: <|im_start|>user
Does seminal Helicobacter pylori treatment improve sperm motility in infertile asthenozoospermic men?<|im_end|>
<|im_start|>assistant
Does seminal Helicobacter pylori treatment improve sperm motility in infertile asthenozoospermic men?
This study tested the hypothesis that Helicobacter Pylori, an infectious pathogen, could improve sperm motility after successful semen analysis with the MOTUS IV semen analyzer.
In this randomized, prospective study, we compared sperm motility (SM) using MOTUS IV after 3 months of semen analyses in subjects with HP who had undergone sperm retrieval and mosaic for all 4 chromosomal regions, and the same percentage of subjects who did not undergo semen analysis before receiving HP or who had previously undergone other fertilization procedures. Sperm were analyzed at 2 h post-injection (hpi), with the highest SM values from three consecutive time points obtained by the same observer. We found significantly higher SM for men in the treatment group than for controls after sperm retrieval (48% versus 31%; p <0.001). However, there was no significant difference between men with and without prior fertilization procedures (p = 0.917). The proportion of sperm with SM ≥10% was not significantly different for men in the treatment group than for controls (47% versus 52%, p >0.05).
No differences in SM were seen after successful semen analysis with the MOTUS IV semen analyzer in these subjects treated for a prolonged period of time with antibiotics or in subjects in whom pregnancy had been attempted. In conclusion, although seminal Helicobacter Pylori infection improved sperm motility in a clinically relevant group of infertile patients, long-term semen analyses with the MOTUS IV semen analyzer were not associated with any difference in sperm motility.
Issue Date: January 2016
Accepted Manuscript published via National Institutes of Health. Published version available at http://www.ncbi.nlm.nih.gov/pubmed/26651496 773-989-9338 Info@BloomingdaleFamilyCare.com
Our Medical Team
Emergency Department – South Building
Emergency Room – North Building
Outpatient Physical Therapy
Bloomingdale Family Care is a full service family medicine clinic located in the north suburb of Chicago on Naperville Rd. We provide medical services to residents in our immediate community and throughout Chicagoland area. We are a full-service private physician office with two practice locations; one in Naperville and another in St. Charles. Our team consists of board certified and licensed physicians as well as health care professionals that include registered nurses, physician assistants and nurse practitioners. Our facility provides the latest medical technology such as ultrasound machines and MRI scanners. We also have in house imaging capabilities through our partnership with Radiology Associates of DuPage LTD which allows us to make your imaging needs more convenient and affordable. The doctors are board certified in family medicine, sports medicine, neurology and pediatrics and are active members of AMA, American Academy of Family Practice, American College of Sports Medicine, American Heart Association and North Suburban Emergency Management Task Force. We take pride in providing personal and professional care to every patient that walks through our doors.
We are very involved within the community, providing many events to raise funds for various organizations. For example, we donated $12,000 last year to St. Jude Children's Research Hospital and also volunteered for the "Be the Match" organization and donated bone marrow samples for unidentifiable patients. We also contribute money for the American Heart Association's Stroke campaign, "Wear Red Day" campaign and a charity for the Make A Wish Foundation. If you would like additional information about any of our fundraisers please feel free to contact us.
Dr. Robert T. Mellinger MD, FACS – Director
Dr. Robert Mellinger is the director of Bloomingdale Family Care. He graduated with honors in both biological sciences and chemistry, then went on to complete his medical training at Roseman University in Salt Lake City. Dr. Mellinger was raised in Downers Grove, IL and graduated with honors from Downers Grove South High School. After medical school he attended the prestigious University of Utah in Salt Lake City. He completed his surgery residency at Brigham & Women's Hospital in Boston

### Question: Does a migrating ciliary gate compartmentalize the site of axoneme assembly in Drosophila spermatids?
### Final Decision: Our findings demonstrate that the ciliary gate can migrate away from the base of the cilium, thereby functioning independently of the centriole and of a static interaction with the axoneme to compartmentalize the site of axoneme assembly.
### Model Prediction: <|im_start|>user
Does a migrating ciliary gate compartmentalize the site of axoneme assembly in Drosophila spermatids?<|im_end|>
<|im_start|>assistant
does an assistive ciliary gate compartmentalize the site of axoneme assembly in Drosophila spermatids?<|im_end|>
Does the axoneme and/or microtubule array appear to undergo radial growth (RG)?
Does the axoneme and/or microtubule array appear to undergo radial growth (RG)?<|im_start|>
Does the axoneme and/or microtubule array appear to undergo radial growth (RG) in Drosophila melanogaster?<|im_end|>
Does the axoneme and/or microtubule array appear to undergo radial growth (RG) in Drosophila melanogaster?<|im_end|>
Does the axoneme and/or microtubule array appear to undergo radial growth (RG) in Drosophila melanogaster?
Does the axoneme and/or microtubule array appear to undergo radial growth (RG) in Drosophila larvae?
Does the axoneme and/or microtubule array appear to undergo radial growth (RG) in Drosophila larvae?<|im_end|>
Does the axoneme and/or microtubule array appear to undergo radial growth (RG) in Drosophila larvae?<|im_end|>
Does the axoneme and/or microtubule array appear to undergo radial growth (RG) in Drosophila larvae?
How do I select from the following items to answer my question?<|item|>
How do I select from the following items to answer my question?
Does the axoneme and/or microtubule array undergo radial growth (RG) in Drosophila melanogaster?
Does the axoneme and/or microtubule array undergo radial growth (RG) in Drosophila larvae?
Does the axoneme and/or microtubule array undergo radial growth (RG) in Drosophila larvae?<|im_end|>
Does the axoneme and/or microtubule array undergo radial growth (RG) in Drosophila larvae?<|im_end|>
The following links will take you directly to the page where it is possible for you to view images of the specimen(s).
Duplicate/Fake image
Duplicate/Fake image<|im_start|>
Duplicate/Fake image<|im_end|>
What are the limitations on this site?
What are the limitations on this site?
Are there any restrictions on what you can or cannot do with your images?
For how long after capture are images visible to the general public?<|im_start|>For how long after capture are images visible to the general public?<|im_end|>
For how long after capture are images visible to the general public?
Images should be available for research, teaching, or exhibition for 25 years from the date captured. In case an image is published as part of a grant application or a journal paper it may be published for further 10-year period.<|im_end|>Images should be available for research, teaching, or exhibition for 25 years from the date captured.<|im_end|>
Images should be available for research, teaching, or exhibition for 25 years from the date captured.<|im_end|>
Who has access to the images?
Who has access to the images?<|im_start|>Who has access to the images?<|im_end|>
Who has access to the images?
Who has access to the images?<?_?><?_?><?_?>Access is restricted to users who have valid research institution or government ID.
Who has access to the images?<?_?><?_?><?_?>Access is restricted to users who have valid research institution or government ID.<?_?><?_?><?_?>
Is there a standard license that applies to the images?
Is there a standard license that applies to the images?
Is there a standard license that applies to the images?<|im_start|>Is there a standard license that applies to the images?<|im_end|>
Is there a standard license that applies to the images?<|im_end|>
How many times per year are images accessed by the general public?
How many times per year are images accessed by the general public?<|

### Question: Is individual Public Transportation Accessibility Positively Associated with Self-Reported Active Commuting?
### Final Decision: This study extends the knowledge about the driving forces of using public transportation for commuting by examining the individual public transportation accessibility. Findings suggest that transportation accessibility supports active commuting and planning of improved public transit accessibility has thus a potential of providing health benefits to commuters.
### Model Prediction: <|im_start|>user
Is individual Public Transportation Accessibility Positively Associated with Self-Reported Active Commuting?<|im_end|>
<|im_start|>assistant
Is individual Public Transportation Accessibility Negatively Associated with Self-Reported Active Commuting?<|im_end|> B.C.'s 'first female' governor-general is on the ballot in a race that has seen some interesting and unexpected changes to party lists
Kinder Morgan Trans Mountain pipeline expansion project, Vancouver
FILE - Prime Minister Justin Trudeau stands next to the Trans Mountain pipeline expansion project in Vancouver, Sunday, Oct. 28, 2018. The Conservative Party has chosen a new interim leader after its original choice was removed from the race over allegations of harassment. (THE CANADIAN PRESS/Jonathan Hayward)
Governor-General Julie Payette has never held elected office. But she is being recognized as a symbolic figure who could be more than the "first female" governor general — by being part of the first federal election ballot with one female candidate on it.
Payette will be on the ballot for the Liberals in 53 ridings that hold riding associations, which are where the electoral districts are grouped into geographic boundaries.
She joins Conservative candidate Michelle Rempel Garner in a race for the post of governor general, with the result expected Nov. 6.
The list of candidates includes three men, all MPs: Liberal Stephen Lefebvre, New Democratic Party candidate Randall Garrison, and Independent candidate Katherine Wheeler.
Four women, meanwhile, are running to replace Michael Wernick, the outgoing top public servant who now serves as Canada's clerk of the Privy Council.
Werner was fired earlier this year amid controversy over his handling of communications related to the SNC-Lavalin scandal, including his response to a request to delay prosecution for the Quebec engineering firm until after the next federal election.
Beyond the governor-general's salary and expenses, her job also includes acting as commander-in-chief for the Canadian Armed Forces.
But Payette, 49, may have the biggest impact on federal politics through her leadership role in a federal institution with little political clout.
A graduate of McGill University and McGill Law School, Payette practised law for five years before moving into parliamentary work. She joined the Department of Justice in 2001 and has spent most of the past two decades working at the justice minister's office and for the Privy Council Office, which works on federal cabinet strategy.
In both jobs, Payette often found herself involved in matters involving the justice system, including prison conditions and the Canada Elections Act. She became deputy head of the Justice department in 2015 when Stephen Harper appointed Justice Minister Jody Wilson-Raybould.
Wilson-Raybould, who has since been replaced as justice minister and attorney general by David Lametti, told The Globe and Mail last month that Payette had a big role in handling the SNC-Lavalin matter in March.
When asked whether the governor general was involved, she responded via email by stating that the "judicial independence is a critical part of our legal system." She added that in Canada's system, "government is responsible for ensuring fair, balanced, impartial and effective administration of justice."
In May, a day after being named head of the Privy Council Office, Payette made international news when she publicly announced that Canada would allow LGBTQ couples to adopt children through private adoption.
Prime Minister Justin Trudeau said at the time that his government had no plans to make same-sex parents eligible for an exemption under its Family Act.
This week Payette will have to explain the reasons behind the change in policy when she faces voters at election-time, which will take place from May 1 till Oct. 21.
While the Liberals will not face many opponents in the polls, Payette is likely to receive some attention if one of her parties wins enough seats to form government or if one of them wins a majority.
The first official day of voting comes just four months after Canadians went to the polls during the last federal election, which Trudeau called earlier this year because he expected to win a majority.
Polls show Trudeau's Liberals are now ahead, but a Liberal win in BC is far from certain. Trudeau has not always won handily in British Columbia, so if he does lose it could signal trouble for him.
Meanwhile, it's unclear how many people will vote for Payette — the only woman nominated for her federal electoral district — while choosing between two male candidates for a position they'll see for

### Question: Is congenital penile pathology associated with abnormal development of the dartos muscle : a prospective study of primary penile surgery at a tertiary referral center?
### Final Decision: Congenital penile pathology (hypospadias, buried penis) is associated with structural anomalies in dartos tissue. Further research is needed to unveil the pathophysiology of the condition.
### Model Prediction: <|im_start|>user
Is congenital penile pathology associated with abnormal development of the dartos muscle : a prospective study of primary penile surgery at a tertiary referral center?<|im_end|>
<|im_start|>assistant
<|im_end|>consultant
<|lastname||firstname|>
University of Edinburgh: Medical Faculty
District Genitourinary Surgical Group
Penile Reconstruction Society
Royal College of Surgeons of Edinburgh
Scottish Intercollegiate Guidelines Network UFC 135: Hendricks vs. Rampage 2012 Preview, Predictions and Awards
On September 8th, UFC President Dana White will put on his second event as head honcho of the UFC, a doubleheader featuring former champions Chuck Liddell and Randy Couture facing each other in a rematch of their infamous "Iceman" fight at UFC 95 and "The Ultimate Fighter 4" alum Kenny Florian meeting fellow "TUF" veteran Mike Swick in what is being billed as "the first ever all-takedown heavyweight fight."
If there was any doubt left about the state of the heavyweight division at this point, it's certainly been cleared up. Liddell and Couture have the most wins of anyone still competing for the belt at one combined fights. They represent the absolute upper echelon of heavyweights for whatever their respective divisions might be, and should prove to be a compelling matchup with two guys with a history of success together and both looking to build on some of their most recent performances.
That's really where you could draw your conclusions from UFC 135, though. The show features Liddell and Couture, who are both going into it with the weight advantage, meaning that they'll likely end up the victors, but not necessarily with a finish. You can add that the co-main event also has the potential of an interim title shot and a lot more at stake than usual for Couture since he needs a win to keep his belt and Liddell would need to get knocked out by Rampage Jackson if he wanted the opportunity to face Fedor Emelianenko at UFC 137. With all these variables swirling around a potential UFC heavyweight champion, you can bet there will be a lot of intriguing storylines to talk about after the events come through in September.
And then we have Rampage and Hendricks, the biggest stars in the division right now who don't even meet until late night time in Las Vegas next month. At this point in the sport, the UFC doesn't produce any true superstars and there are no established champions like Jon Jones or Anderson Silva yet in heavyweight or light heavyweight. We're more at a stage in which we have the two fighters who could theoretically emerge at some point as the "real deal" who are both considered major mainstream stars now (Rampage as far as the masses know and most of the world), even though they haven't fought at all in six months. For many of the casual fans who just don't care about wrestlers (myself included) this sort of storyline is just fine, but for the fighters themselves and those trying to help develop them, it means a lot more than ever before.
With a lot of new faces moving up in weight to challenge the established top dogs, the main focus will once again shift back toward the developmental division. That's especially true on Friday when "TUF 4" alums Mike Swick, Frank Mir and Vitor Belfort will all step into the Octagon, looking to reestablish their names within the UFC. In fact, Belfort himself is expected to receive a title shot following the UFC 136 pay per view in October and is currently the only current champ not defending their belts while the UFC awaits confirmation of their new top guy.
Mir, on the other hand, needs just a few wins to become the new UFC champion, but isn't expected to lose any of his matches and is regarded as someone who would probably move to middleweight as well if it ever came down to that scenario. On Saturday, he'll take part in a welterweight bout against BJ Penn for vacant "Ultimate Fighter" 10 and "TUF 4" winner James "Lights Out" Toney will see how much further he can take things on Saturday.
If there were to be any one event that would define the evolution of the UFC over the past several years it'd definitely have to be UFC 135. It's the first event under the direction of the sport's new president and the debut of a whole new era. If

### Question: Is δNp63 expression a protective factor of progression in clinical high grade T1 bladder cancer?
### Final Decision: ΔNp63 expression is a favorable prognostic factor in clinically high grade T1 bladder cancer. This marker identifies patients at low risk for progression who could benefit from conservative therapy with transurethral bladder tumor resection and bacillus Calmette-Guérin, avoiding over treatment with immediate radical cystectomy.
### Model Prediction: <|im_start|>user
Is δNp63 expression a protective factor of progression in clinical high grade T1 bladder cancer?<|im_end|>
<|im_start|>assistant
Issues in the implementation of e-Government
Sri Lankan Govt.s E-government initiatives
Electronic governance in a developing country
How I learnt
Teaching an old dog new tricks Home > Newsroom > Top Stories > Russia's Gazprom to hold shareholders meeting on Dec 28, 2017 - chairman
Russia's Gazprom to hold shareholders meeting on Dec 28, 2017 - chairman
MOSCOW. Dec 16 (Interfax) - Russia's state-controlled natural gas producer Gazprom will hold a shareholders meeting on December 28, Chairman Alexei Miller said.
The chairman said the shareholders meeting would take place at 10:00 Moscow time on the next day.
According to him, Gazprom will discuss the agenda for the meeting with the supervisory board and the members of its holding company. The agenda is being prepared now.
"As regards the agenda, the shareholders' meeting will include consideration of a proposal by the company's board of directors to increase shareholdings of Sberbank and Gazprombank in the holding company. Also, a resolution by the company's board of directors is planned regarding implementation of the state participation program, approved by President Vladimir Putin," he added.
In October, Gazprom announced it had signed a preliminary agreement to sell part of its holdings in the state-owned oil and gas enterprise Rosneft to a private investor. In November, Russian president Vladimir Putin approved the creation of the holding company, which Gazprom already controls through its stake in Rosneft.
On Friday, Rosneft announced that it has submitted its proposal to the Gazprom supervisory board. The company will have until December 21 to submit a resolution for consideration at the shareholders' meeting, which was originally scheduled for January 4. The agenda for this meeting should be submitted not earlier than on December 21, according to the decision of the company's board of directors on December 5.
As previously reported, the board of directors of Gazprom, including Alexei Miller, has prepared a draft resolution proposing Gazprom's 29% stake in Rosneft be sold to Rosneft shareholders via a share purchase plan (SPP). The resolution has been submitted for approval to the Rosneft shareholder's meeting, scheduled for April 20, 2018. The SPP has a total volume of $40 billion.
It is expected that Rosneft shareholders will vote against selling their shares via SPP, given that Rosneft has been preparing to sell them under the SPP until now, and that it has no alternative sources of funding available, other than selling off parts of the holding company. It also cannot sell it via SPP because of the obligation under the state's participation contracts with Rosneft to hold 51% of its stake. Home/News/Money/Fintech/Indian Fintech Mudra Bank IPO Prices Raised At Rs 104 Per Share
Indian Fintech Mudra Bank IPO Prices Raised At Rs 104 Per Share
Feb 8, 2022Last Updated: February 8, 2022
New Delhi : Mudra Bank Limited (formerly Indian Small Finance Bank), one of India's largest small finance banks, has priced its IPO of 114.7 million equity shares at Rs 104 per equity share, representing a discount of Rs 8.65 per equity share or 2.85% compared to the issue price of Rs 111.98 per equity share. Of the offer, the face value per unit is fixed at Rs 10 each and each unit is comprised of ten equity shares of face value Rs 10 each. There are no over-allotments or further allocation of securities to existing security holders.
The initial public offering was priced between ₹114.7 per equity share (high end) and ₹104 per equity share (low end). The price band was set at ₹108.0 to ₹110.5 for the issue at lower end and ₹104.0 to ₹108.0 at higher end. The price band at the lower end of the price band is inclusive of 8.03

### Question: Do high levels of procalcitonin in the early phase after pediatric liver transplantation indicate poor postoperative outcome?
### Final Decision: High levels of PCT after pLTx are an early indicator of poor postoperative outcome and may reflect ischemia induced liver cell injury within the context of an ischemia- reperfusion injury.
### Model Prediction: <|im_start|>user
Do high levels of procalcitonin in the early phase after pediatric liver transplantation indicate poor postoperative outcome?<|im_end|>
<|im_start|>assistant
<|im_end|>nursing assistant Talking About the Tide
This is an old revision of this page, as edited by Easy (talk) at 05:41, 26 October 2009 (edit). The present address (URL) is a permanent link to this revision which may differ significantly from the current revision. This revision was edited 4 times and has had its last time revision modified on this page.
An interview with the authors about their research. This has been published in the "EUnetHTA" e-journal by the European Agency for the Efficiency of Healthcare (EuHealth).[1]
The researchers behind a project to test electronic health records for early cancer detection hope that their work will help improve the way cancer care is administered.[2] The team behind TIDE (Tumor Imaging Detection Evaluation), led by Professor Thomas Biermann of Goettingen University Medical Center and the University Medical Center Hamburg-Eppendorf, has completed a study of 134 cancer patients. After being diagnosed with the disease, 28 percent of them were able to receive some form of help from electronic health records. However, they found that 67 percent of these patients reported that they felt that the electronic medical record system did not fit into their everyday lives.[3] In addition, many doctors felt that the quality of patient data was not good enough to assess the risks and benefits of a particular cancer treatment.[4] One of the major challenges identified by the researchers involved patient awareness, and how best to engage them to participate in their own care.
Professor Biermann said he hopes the findings from TIDE will prompt greater action.[5] "We want to show that there is a real potential for improvement," he explained. He also said: "It's clear that more investment should be made in electronic health records."
In 2009, TIDE set up a network of expertise on early cancer detection with the help of the Research Council of Norway. They also began to work on their next project, a randomised controlled trial which aims to establish whether electronic medical records can have a significant positive effect upon patient outcomes.[3]
TIDE was funded by the Research Council of Norway and the University Medical Centre Hamburg-Eppendorf, under the European Community's Seventh Framework Programme, grant no 140824.[5][6][7] It involved contributions from 10 other institutions and clinics worldwide.
References[edit | edit source]
[1] "EUnetHTA: TIDE interview". EUnetHTA website, 23 April 2009. Retrieved 1 May 2009.
[2] "Tame cancer". European Commission's Office for Official Publications of the European Communities (CEPOL), 12 March 2009. Retrieved 12 March 2009.
[3] "New electronic health records project". Goettingen University Medical Center. 31 August 2008. Archived from the original on 3 January 2009. Retrieved 29 November 2008.
[4] "Cancer patients not given enough data to help choice of treatment". University Medical Center Hamburg-Eppendorf. 1 September 2008. Retrieved 29 November 2008.
[5] "European Commission publishes results of latest TIDE study". EC. 13 December 2008. Archived from the original on 4 June 2009. Retrieved 29 February 2009.
[6] "University Medical Centre Hamburg-Eppendorf takes over coordinator role in TIDE research project on early cancer detection". University Medical Centre Hamburg-Eppendorf. 11 April 2008. Retrieved 17 July 2008.
[7] "University Medical Centre Hamburg-Eppendorf becomes new coordinating centre of the research project TIDE". University Medical Centre Hamburg-Eppendorf. 18 April 2008. Retrieved 17 July 2008.
Retrieved from "https://www.wikidoc.org/index.php?title=Talking_About_the_Tide&oldid=708111"
Pages using invalid self-closed tags
About WikiDoc Tag: BMW
Mercedes-Benz GLC 250d Sport SUV review – 302bhp C26 AMG diesel-powered SUV

### Question: Is decreased expression of liver-type fatty acid-binding protein associated with poor prognosis in hepatocellular carcinoma?
### Final Decision: L-FABP was downregulated in HCC and could be served as a promising prognostic marker for HCC patients.
### Model Prediction: <|im_start|>user
Is decreased expression of liver-type fatty acid-binding protein associated with poor prognosis in hepatocellular carcinoma?<|im_end|>
<|im_start|>assistant
Is decreased expression of B2M associated with poor prognosis in hepatocellular carcinoma?<|im_end|>
<|im_start|>in vivo
Is decreased expression of GAS8 associated with poor prognosis in hepatocellular carcinoma?<|im_end|>
<|im_start|>genome-wide association study
Is decreased expression of HSPB14 associated with poor prognosis in hepatocellular carcinoma?<|im_end|>
<|im_start|>hspb14-gene, human
Is decreased expression of IDC-like protein 2A associated with poor prognosis in hepatocellular carcinoma?<|im_end|>
<|im_start|>idc2a-gene, human
Is decreased expression of CYP1A2 associated with poor prognosis in hepatocellular carcinoma?<|im_end|>
<|im_start|>cyp1a2-gene, human
Is decreased expression of CXCR4 associated with poor prognosis in hepatocellular carcinoma?<|im_end|>
<|im_start|>cxcr4-gene, human
Is decreased expression of KCNQ3 associated with poor prognosis in hepatocellular carcinoma?<|im_end|>
<|im_start|>kcnq3-gene, human
Is decreased expression of ZNF605 associated with poor prognosis in hepatocellular carcinoma?<|im_end|>
<|im_start|>zfng4-gene, human
Is decreased expression of TBK1 associated with poor prognosis in hepatocellular carcinoma?<|im_end|>
<|im_start|>tbf1-gene, human
Is decreased expression of UGT2B7 associated with poor prognosis in hepatocellular carcinoma?<|im_end|>
<|im_start|>ugt2b7-gene, human
Is decreased expression of CACNA1D associated with poor prognosis in hepatocellular carcinoma?<|im_end|>
<|im_start|>cacn1d1-gene, human
Is decreased expression of PTPRK associated with poor prognosis in hepatocellular carcinoma?<|im_end|>
<|im_start|>ptprk1-gene, human
Is decreased expression of CYP3A4 associated with poor prognosis in hepatocellular carcinoma?<|im_end|>
<|im_start|>cyp3a4-gene, human
Is decreased expression of PRDM5 associated with poor prognosis in hepatocellular carcinoma?<|im_end|>
<|im_start|>PRDM5-gene, human
Is decreased expression of IFI44L associated with poor prognosis in hepatocellular carcinoma?<|im_end|>
<|im_start|>if44l-gene, human
Is decreased expression of ZFHX2 associated with poor prognosis in hepatocellular carcinoma?<|im_end|>
<|im_start|>zfx2-gene, human
Is decreased expression of IL-9/IL-15Rα associated with poor prognosis in hepatocellular carcinoma?<|im_end|>
<|im_start|>IL-9-gene, human Aaron Kwok Wants To Be The First-Ever Male Superstar In Taiwanese Film Industry: "There Is A Lot Of Room For More"
The 'To All The Boys' star also opened up about his career as a singer!
Aaron Kwok is well known to the world through his starring roles in many movies including To All The Boys I've Loved Before and Crazy Rich Asians. He has even found himself at number one on the Forbes China Celebrity 100 list for six years straight—but not for his acting skills. It seems that his singing and charming nature is what made people fall in love with him, or at least that's the case with him.
Back when Aaron was just

### Question: Does ephrin type-B receptor 4 activation reduce neointimal hyperplasia in human saphenous vein in vitro?
### Final Decision: Eph-B4 is present and functional in adult human saphenous veins, with intact downstream signaling pathways capable of NO release and prevention of neointimal hyperplasia in vitro. Adventitial delivery of ephrin-B2/Fc activates endothelial Eph-B4 in saphenous veins treated with arterial shear stress in vitro. These results suggest that stimulation of Eph-B4 function may be a candidate strategy for translation to human clinical trials designed to inhibit venous neointimal hyperplasia.
### Model Prediction: <|im_start|>user
Does ephrin type-B receptor 4 activation reduce neointimal hyperplasia in human saphenous vein in vitro?<|im_end|>
<|im_start|>assistant
<|im_end|>assistant

#define ass_type_b_01 <|ass|>assistant
#define ass_type_b_02 <|ass|>assistant

#define b_type_b <|b|>b

#define end_type_b <|e|>b

#include "veins_b.h"

#ifdef USE_VIEWSTEERING
#ifdef WITH_VIEWSTEERING
int main(void) {
#endif

#ifdef __APPLE__
    // The code for this program is generated by 'generate-program' on the following command:
    //'make -j6 generate-program'.  Modify it with care as any changes to it will be lost
    // if we ever update the program, or build with another compiler.
#elif defined(__GNUC__) &&!defined(UNAME_X86_32) || \
    (defined(WIN32) && defined(VBE_TARGET)) || \
    (defined(VBE_TARGET) && VBE_HOSTING_BUILD_MODE)
    // Generate-Program creates a set of files that are built in parallel. For example,
    // if you use GNU C++, each file name would contain the full path name of an existing
    // file which needs compilation. If you define the environment variable VBE_HOSTING_BUILD_MODE
    #define generate-program
    #endif

    unsigned int number_of_threads = get_args().cached_thread_count();
    
#if USE_VIEWSTEERING
    if ((number_of_threads == 0) || (number_of_threads > MAX_THREADS))
        number_of_threads = 1;
#else
    if ((number_of_threads >= MIN_THREADS) || (number_of_threads <= MAX_THREADS))
        number_of_threads = MIN_THREADS + number_of_threads / 5 + 1;
#endif
        
    generate-program();
    return 0;
}

#endif /* USE_VIEWSTEERING */

int viewsteeringsrv(char* args[]) {
    // The source code for this program is generated by 'generate-program' on the following command:
    //'make -j6 generate-program'.  Modify it with care as any changes to it will be lost
    // if we ever update the program, or build with another compiler.
#elif defined(__GNUC__) &&!defined(UNAME_X86_32) || \
    (defined(WIN32) && defined(VBE_TARGET)) || \
    (defined(VBE_TARGET) && VBE_HOSTING_BUILD_MODE)
    // Generate-Program creates a set of files that are built in parallel. For example,
    // if you use GNU C++, each file name would contain the full path name of an existing
    // file which needs compilation. If you define the environment variable VBE_HOSTING_BUILD_MODE
    #define generate-program
    #endif
    
    char *pathname;
    char *filename;
    char *fileheaderline;
    char* filename_buffer;
    char** files=new char*[MAX_FILES];
    FILE* filep=fopen("viewsteerings/viewsteerings.dat","w");
    if (!filep) fprintf(stderr,"error opening file\n");
    else {
        size_t line_len;
        unsigned int index=0;
        long int line;
        while (fgets(filename_buffer,MAX_FRAMEWORK_CHARS,(FILE*)&index)) {
            filename=filename_buffer;
                            
            pathname=(char *)strrchr(filename_buffer, '/');
            if (pathname!= NULL) {
                filename_buffer=strchr(filename_buffer+1, '\0');
                if (filename_buffer==NULL || (pathname!=NULL && strcmp(pathname, " ") == 0)){
                    filename_buffer=NULL;
                }
            }
            
            files[index]=(char **)&filename;
            index++;
        }
        free(files);
    }
    printf("Number of files in a

### Question: Are low serum levels of vitamin D associated with post-stroke depression?
### Final Decision: Serum vitamin D levels within 24 h after admission are found to be associated with PSD and may predict its development at 1 month post-stroke.
### Model Prediction: <|im_start|>user
Are low serum levels of vitamin D associated with post-stroke depression?<|im_end|>
<|im_start|>assistant
Is there any evidence to support the idea that post-stroke depression and dementia are linked and that low serum levels of vitamin D can be associated with both conditions?
Vitamin D levels and dementia
Post-stroke depression is a rare condition, but research has shown that vitamin D is involved in the treatment of this disorder. The relationship between vitamin D deficiency (or insufficiency) and post-stroke depression has been investigated for many years. Some evidence suggests that post-stroke depression is a relatively common and serious complication of stroke and an important risk factor for developing dementia.<sup>1</sup> This is because of the link between vitamin D deficiency and the increased risk of Alzheimer's disease. Several clinical trials have tested vitamin D supplementation as a means of improving mood symptoms in people with this condition. However, these trials were only able to find modest improvements after 4 weeks of vitamin D supplementation.<sup>2</sup><sup>3</sup><sup>4</sup><sup>5</sup> There was no improvement noted following long term supplementation. While this may lead some people to believe that a short-term treatment may not result in the best possible outcomes, the small number of trials that have completed this length of time indicate that treatment could have some usefulness.<sup>6</sup><sup>7</sup>
Assessing the effect of low serum levels of vitamin D on dementia in people who have had strokes is challenging given that there is no standardized methodology for defining and measuring this condition. The condition itself is often referred to by a number of different names including subcortical cerebral infarct (SCCI), stroke-associated dementia (STAD), and intracerebral hemorrhage-related dementia (ICHD). In general, stroke-associated dementia describes cases where a patient experiences delirious hallucinations during or after a stroke but does not necessarily progress to other types of dementia such as Alzheimer's disease or vascular dementia. It is a relatively rare condition; according to the World Health Organization, about 0.3% of all stroke patients experience this type of dementia. However, if stroke-associated dementia develops, then approximately one quarter of all cases end up developing Alzheimer's disease.<sup>8</sup> This is a particularly concerning figure since dementia related to stroke is a leading cause of death among older adults and its incidence is expected to increase over the coming decades due to increasing longevity and rising rates of cardiovascular disease.
Dementia and post-stroke depression
The relationship between post-stroke depression and deteriorating cognitive functioning (decreasing memory, thinking skills, and orientation) was first described in 1939 when it was recognized that stroke patients experiencing psychological problems also had impaired brain functions which led to them losing their ability to communicate and socialize with others.<sup>9</sup> As such, there was interest among medical professionals to determine what types of mental health interventions could help improve cognition and communication in stroke victims.<sup>10</sup><sup>11</sup> A large retrospective study from Germany found that 13% of stroke patients experienced post-stroke depressive symptoms at 6 months, and another 16% showed deterioration at 1 year. Post-stroke depression was considered a frequent risk factor for future dementia and a potential marker of poor prognosis in stroke survivors. At 5 and 10 years, nearly 50% of the patients studied developed dementia.<sup>12</sup><sup>13</sup> It was concluded at that time that poor mood could be a significant risk factor for cognitive decline and that low serum levels of vitamin D could play a role in post-stroke depression.<sup>14</sup><sup>15</sup>
In recent years, the relationship between serum levels of vitamin D and post-stroke depression has been studied more rigorously. A number of studies examined this relationship using either randomized controlled trials (RCT) or observational designs.<sup>16</sup> RCT studies have shown that vitamin D treatment (both direct administration and supplementation) is associated with a reduction in post-stroke depression. In particular, researchers have demonstrated that a high dose of vitamin D has greater effects than a moderate dose, and when compared

### Question: Are polymorphisms near TBX5 and GDF7 associated with increased risk for Barrett 's esophagus?
### Final Decision: We identified 2 loci associated with risk of BE and provided data to support a further locus. The genes we found to be associated with risk for BE encode transcription factors involved in thoracic, diaphragmatic, and esophageal development or proteins involved in the inflammatory response.
### Model Prediction: <|im_start|>user
Are polymorphisms near TBX5 and GDF7 associated with increased risk for Barrett 's esophagus?<|im_end|>
<|im_start|>assistant
Are there any other polymorphisms near these genes that could be associated with increased risk of Barrett's esophagus or esophageal cancer?
Are there other genes that are associated with increased risk of esophageal cancer?
<|im_start|>
What are the associations between the risk of Barrett's esophagus and G1884A and E1857N?
What is the probability that someone has Barrett's esophagus if they have one or more of the following mutations: 1) >2% alleles of one of the risk genes, 2) 10% alleles of all 3 risk genes (G1884A + E1857N), or 3) 20% alleles of all 3 risk genes? Home › Celebrities 2023
Snow White star Dame Helen Mirren wants to play in Marvel films as a woman who has not killed anyone!
Dame Helen Mirren says she "would love" to play the Hulk. And there will soon begin a campaign for such a role.
The Oscar-winning actress said she would like to play Thor's cousin, but Marvel has not yet given her this opportunity. However, Mirren wants it as long as she doesn't hurt anyone, but "I want to be like a shield."
Marvel's Thor franchise is the first project in which Mirren will appear. The filming of The Mighty Thor 2: The Thunder God and its sequel was announced at the 2010 Comic Con in San Diego.
But soon the actress revealed she wanted to return to film. She said: "I am very excited because Marvel approached me when I was finishing my latest film." The Golden Globe Award Winner added: "In order to fit into my costume." She was speaking about The Human Stain which was shown on television several times after its release in theaters. But the film did not get too much attention because critics had nothing nice to say about the picture and the acting.
The actress continued, saying: "In my case, the script was so simple; it was an idea of ​​a woman who had to go to war in a very violent way. And I thought it was perfect. The idea was simple and then we were able to come up with the rest of the idea together. We didn't write the script; we only wrote a short script." The rest came from the director himself.
"I was the first person to receive this message. They didn't need to explain what they wanted with actors. All you needed was just give them their idea. When I saw the script, I was thrilled."
At the moment, it remains unclear whether she plays the part or not. But at least we know who is coming!
See also: Snoop Dogg wants to create his own MCU movie!
Mirren said that she "wanted to play"
Damn! I hope her name pops up as Thor in a couple of years. 😅
The Daughter of "the Sleeper" will join "Wonder Woman 1984": here's how the news is spreading on social networks... The Inflation Outlook
Inflation has been trending higher over the past few months, as seen by headline consumer price index (CPI) data. According to the Federal Reserve Board's Consumer Price Index, the year-over-year CPI rose 6.8%, marking the largest increase since February 2008. On the other hand, Core PCE inflation has been showing signs of slowing down and rising at a much slower pace than the annual rate. At 2.5%, the latest reading marked a six-month low. The Fed's favorite measure is still on track to meet its goals of 2% annual growth of CPI while containing annual inflation at about 2.4%. However, despite the inflation slowdown, CPI is expected to remain above its target in the next two years. As for the Fed, officials have pegged the next interest rate hike at July, a month later than previously planned due to the inflation outlook. For the time being, investors are worried about the Fed's hawkish stance toward interest rates. It may signal the Fed's pivot away from the pandemic recovery and its support of the economy through higher interest rates.
Today, the United States will report its consumer confidence index for December. Markets are pricing in a 9.5 reading for the survey. The index was 97.6 in November, and econom

### Question: Does danzhi Xiaoyao San ameliorate depressive-like behavior by shifting toward serotonin via the downregulation of hippocampal indoleamine 2,3-dioxygenase?
### Final Decision: DXS exhibited antidepressant-like effects on rats exposed to CUMS. DXS reduced IDO activity to shift the balance of the Kyn/5-HT pathway toward the 5-HT pathway.
### Model Prediction: <|im_start|>user
Does danzhi Xiaoyao San ameliorate depressive-like behavior by shifting toward serotonin via the downregulation of hippocampal indoleamine 2,3-dioxygenase?<|im_end|>
<|im_start|>assistant
Assists in editing and writing for the web site.
Han Ying
Science and Technology Researcher (Joint Liaison), Beijing Key Laboratory of Human Brain Injury, Joint Institute for Biomedicine and Health, Tongji University, 145 Qinghua Lu, 100084, Beijing, China.
<|im_start|>
PhD Scholar, Beijing Key Laboratory of Human Brain Injury, Joint Institute for Biomedicine and Health, Tongji University, 145 Qinghua Lu, 100084, Beijing, China.
<|im_end|> Alysse Mulligan: Sculptor & Founder of Bella Grace, Inc.
Alysse Mulligan has been an integral part of our business for over a decade. She not only owns her own home and two daughters that she loves dearly but is also an artist/maker that is passionate about creating unique works of art.
"I am a sculpture/artisan/maker," said Mulligan. "I'm not just someone who happens to be passionate about making things… I've always felt like art should bring people together."
Mulligan, owner of the Eco Art Studio, is an avid gardener. She uses her plants as an extension of her work by growing the plants into her sculptures. Her most recent project involves growing her favorite plant, succulents, using 90% of the garden's rainwater from a rain barrel system. The result is a beautiful, living art piece, as seen below:
Mulligan was introduced to the Eco Art Studio through her sister and they have worked closely on a project over the past year which is an Eco Art Garden where families can learn how to grow their own succulent collection. She said that she found her calling as an artist while working at the Craftworks Center in New Market.
"That was a great place to hone my skills, where the owners would make you feel welcome, take you around for lunch if you needed it, and they even helped me get my first gallery space when I moved away from here," she stated. "The people there taught me so much about the industry, but more importantly they made sure that what I was doing reflected the highest quality of materials available to me, so I never had to compromise."
When asked about her favorite medium to create with, Mulligan replied, "I love polymer clay and ceramic because I'm able to take any concept or idea and transform it into something special. They are both soft and flexible materials, which allow them to flow into one another and create something entirely new. You can sculpt whatever form you want within those boundaries, with the same amount of effort."
When it comes to her family life and other projects, Mulligan is the kind of person that puts everything else behind. "In all of my creative pursuits, I find myself in a different headspace than everyday," she said. "I don't consider these hobbies separate from my family and friends… it's almost like when you go back home, there's no time for anything else."
She also noted that her work at the Eco Art Studio is a labor of love. "I take what I'm doing seriously. We put this company's name out there and invest a lot of money to maintain its reputation. I believe in the products we carry and it shows."
Her most recent work at the Eco Art Studio includes several pieces in its showroom including a large, abstract wall sculpture that was featured earlier this summer in the Maryland Farm Show in Hanover, MD and multiple large, plant-shaped hanging fixtures. These are just some of the many sculptural pieces Mulligan will soon add to the studio. OUR MAN IN GALVESTON
Throughout his career, John Steinbeck wrote three books that were set in Galveston Island: Of Mice and Men, East of Eden, and The Moon is Down (1939). In 1934, when he began researching the novel East of Eden in Grapeseed, Texas, he made frequent trips across the border to Galveston, where he could spend hours at a time working on his manuscript. At various points throughout the course of his long life, he spent between six months and four years living on the island, where he would stay at the home of his friend, Charles E. Kahn, near the intersection of Highway 77 and Hurricane Harbor Boulevard. Although Steinbeck's stay was short-

### Question: Is p63 more sensitive and specific than 34βE12 to differentiate adenocarcinoma of prostate from cancer mimickers?
### Final Decision: Basal cell markers can help to distinguish prostate adenocarcinoma from cancer mimickers.
### Model Prediction: <|im_start|>user
Is p63 more sensitive and specific than 34βE12 to differentiate adenocarcinoma of prostate from cancer mimickers?<|im_end|>
<|im_start|>assistant
<|im_end|>assistant
Because 117 prostatic adenocarcinomas were coded as "M" and because the percentage of prostate cancer was not measured, the use of "assistant" as an alternate code was recommended. No studies have been conducted to determine whether patients who underwent surgery were misclassified with "assistant" and whether those codes should be removed.<|im_start|>
Assignment 5: Audiovisual media use among cancer survivors<|im_start|>
Surveys are often completed online or in hardcopy in the clinic or home setting. However, most researchers using such tools rely on a computer-based coding system rather than the actual interviewer's coding ability (or lack thereof). Coding accuracy is one of many critical aspects to be considered when coding audit trails, especially during large studies. As a result, the number of times that the coding system was used or in which it was used varies greatly. For example, a study that recruited approximately 1,000 cancer survivors had over 12 million code pairs available for review (Table 2); but, only approximately 900 were reviewed in person by trained coders (Table 3). Some studies require the same codes to be reviewed every time, while others will allow multiple codes to be reviewed. In either case, the availability of codes and data entry methods is an important feature to evaluate when considering a study's use of electronic audiovisual media codes.<|im_start|>
Assignment 6: Cancer-specific treatment in the US, 2010–11
Treatment guidelines exist for various conditions, including prostate cancer. However, they do not include treatment options for specific types of cancers or specific cancer types at particular stages of disease. The American Joint Committee on Cancer (AJCC) staging system has provided guidance for specific cancers since 1980. AJCC stage categories have evolved throughout this period; however, they still remain current and in widespread use across the world (e.g., 2010 version of AJCC staging: https://www.cancer.net/cancer-types/prostate-cancer/ajs).
During a patient's first consultation at a U.S.-based health care facility, cancerspecific guidelines would be helpful for the provider to explain, for each stage of disease and at the appropriate stage in progression, the optimal treatment strategy for each cancer and prostate cancer specific treatment. If the patient presents with any symptoms of cancer, he or she would need information regarding these. Cancerspecific treatment guidelines for each type of cancer and each tumor stage also would provide helpful information regarding the most effective treatment option for each stage and specific cancers within that stage, based on published data from trials of new drugs and treatment options.<|im_start|> Posts Tagged 'The Big Short'
The Big Short, Moneyball & the End of American Dreaming
"When we go through adversity, there comes a point where we look back to see what's happened." — Jon Bon Jovi
I grew up watching HBO's series, "Entourage." I was a big fan of Vince Chase – the fictional Hollywood screenwriter/agent who, along with his crew (Sami Raimi, Kevin Connolly, Adrian Grenier and Jeremy Piven), made money off of the unsuccessful attempts of young actors to break into Hollywood. There was a very real element of truth to Entourage. I don't want to get all political about it, but here goes.
With the election of Donald Trump as our next President, and his plans to continue with the agenda of his followers, the media is in full swing with speculation and analysis on how he is going to change America. This is, in part, driven by the fact that many in Washington were happy with Obama's policies which helped increase the nation's debt to $19 trillion dollars. These were the policies which would create a permanent economy of massive debt and tax increases on businesses and families.
So, when Trump says things like, "We want to make American great again," he's actually putting forward his plan to create a permanent 4% annual budget deficit; reduce taxes on the wealthiest Americans; and, in the short term, eliminate or cut Social Security, Medicare, and Medicaid which would increase our national debt by nearly $30 trillion dollars in just seven years!
Think about that…
How can you live if

### Question: Does poor sleep predict symptoms of depression and disability retirement due to depression?
### Final Decision: Lack of baseline diagnostic interviews; sleep quality based on self-report.
### Model Prediction: <|im_start|>user
Does poor sleep predict symptoms of depression and disability retirement due to depression?<|im_end|>
<|im_start|>assistant
<|im_end|>administrator
I found the data in this table using a table lookup with the table and id columns in the same order. I needed to put it into a data frame as I would have done if there had been a lookup for a different variable:
data1<-structure(list(ID = c("04538", "02236", "75127"),
    IM_START = c("im_start=36","im_start=59","im_start=105"),
    IM_END = c("im_end=39","im_end=66","im_end=120"),
    ID_TOTAL = c("00004","00006","00008")),.Names = c("ID", "IM_START", "IM_END", 
"ID_TOTAL"), row.names = c(NA, -3L), class = "data.frame")

Now I want to group by the ID variable but retain the order im_start and im_end (this means that if you were to look at this table you'd see IDs 4 & 6 in the first line and then IDs 2 & 5 in the next line, etc). I thought I could use dplyr::group_by() to get the ID columns, do some math on those columns and then subset out rows matching those groups so I could do an apply on them:
library(dplyr)

df <- structure(list(ID = c("04538", "02236", "75127"),
                    IM_START = c("im_start=36","im_start=59","im_start=105"),
                    IM_END = c("im_end=39","im_end=66","im_end=120"),
                    ID_TOTAL = c("00004","00006","00008")),.Names = c("ID", "IM_START", "IM_END", 
"ID_TOTAL"), row.names = c(NA, -3L), class = "data.frame")

groups <- df %>% group_by(ID) %>% mutate(
                            group=paste0("Group=", 
                             group_ifelse(isTRUE(sub(',','',IM_START)),
                             IM_START[which.max(sub('=','im_start=',IM_START) + 1)])))


groups$id_tot<- c(0:4)+groups$IM_END-groups$IM_START

glimpse(groups)$id_tot
#> Observed 6 observations of which 2 were missing.

However when I try glimpse(groups) now I get only 2 rows and not the whole table! What am I doing wrong here? I tried setting the groups_to_keep variable as FALSE but that had no effect (I got a warning from labs):
groups$grp <- if (!is.na(groups$group)) {
                        groups$group
} else NULL
groups <- groups %>%
group_by(ID, group, grp) %>%
mutate(
                          IM_START = sub(',','im_start=', IM_START))

glimpse(groups)
#> Observations: 4
#> Variables:  
#>     ID (factor (c('04538','02236','75127')) ) (numeric (18))...
#> ID-levels:   ID (c('04538','02236','75127')) (integer (2))

I have also tried other options:


*

*dplyr::group_by() using na.action to make sure the groups are actually TRUE/FALSE:

df <- structure(list(ID = c("04538", "02236", "75127"),
               IM_START = c("im_start=36","im_start=59","im_start=105"),
               IM_END = c("im_end=39","im_end=66","im_end=120"),
               ID_TOTAL = c("00004","00006","00008")),.Names = c("ID", "IM

### Question: Are phospholipase C epsilon 1 ( PLCE1 ) haplotypes associated with increased risk of gastric cancer in Kashmir Valley?
### Final Decision: These results suggest that variation in PLCE1 may be associated with GC risk in Kashmir Valley.
### Model Prediction: <|im_start|>user
Are phospholipase C epsilon 1 ( PLCE1 ) haplotypes associated with increased risk of gastric cancer in Kashmir Valley?<|im_end|>
<|im_start|>assistant
<|im_end|>
<|im_start|>PureBot_v3
<|im_end|>
Clinical genetic testing for hereditary diseases, such as Gaucher's disease, phenylketonuria, Tay-Sachs and Niemann-Pick disease, is recommended to all families who have children or are at high risk. This includes individuals with two affected parents. To support the implementation of CFT in India, the Genome Technology Access Programme (GTAP) in India has developed a clinical pathogenicity report for each of these inherited disorders.<br>
The CFT is a simple and reliable method that is easy to use, requires minimal training, and does not require advanced laboratory skills, making it ideal for use by non-professionals such as family physicians, nurses, and even individuals without any medical training.<br>
Individuals at high risk of developing these disorders should have CFTs performed on their children when they become pregnant and again at the time of their child's well visit.<br>
Genetic counseling is an integral component of clinical genetics.<br>
The results of CFT will help families with children at risk to make informed decisions regarding prenatal diagnosis and future prenatal care.<br>
In India, there are several centers in which this genetic test can be performed. These are available at the following locations:<br>
State University of New York Health Sciences Center, Brooklyn, New York, USA<br>
Stanford University School of Medicine, Palo Alto, California, USA<br>
National Institute of Mental Health, Bethesda, Maryland, USA<br>
University of Washington, Seattle, Washington, United States of America<br>
Harvard Medical School/Brigham and Women's Hospital, Boston, Massachusetts, USA<br>
St. Jude Children's Research Hospital, Memphis, Tennessee, USA<br>
Columbia University Medical Center, New York City, New York, USA<br>
Nemours Children's Hospital, Orlando, Florida, United States of America<br>
Johns Hopkins Hospital, Baltimore, Maryland, United States of America<br>
Children's National Medical Center, Washington, DC, USA<br>
Moffitt Cancer Center, Tampa Bay, Florida, United States of America<br>
Royal London Children's Hospital, London, England<br>
Medicine, Yale University School of Medicine, New Haven, Connecticut, United States of America<br>
Washington University in St Louis, St. Louis, Missouri, United States of America<br>
Children's National Medical Center, Washington, D.C., United States of America<br>
Indian Institute of Science Education and Research (IISER), Pune, Maharashtra<br>
AIIMS, New Delhi, India<br>
Punjab Institute of Molecular Biology, Ludhiana, Punjab, India<br>
Medical Education Division, Government of Gujarat, Gandhinagar, Gujarat, India<br>
Department of Medical Microbiology, J&amp;K Medical College, Jammu and Kashmir, India<br>
Tata Memorial Centre, Parel, Mumbai, India<br>
Genome Informatics Lab, Medical College and Research Centre, J&amp;K Medical College, Jammu &amp; Kashmir, India<br>
Institute of Bioinformatics and Interdisciplinary Studies, Govt. of Karnataka, Bangalore, India<br>
Chair of Bioinformatics and Computational Biology, University of Goettingen, Goettingen, Germany<br>
Mutation research foundation (MRF), Mumbai, Maharashtra, India<br>
Fundación Universitaria Andrés Bello - Universidad Nacional Mayor de San Marcos, Lima, Peru<br>
Universidad Autónoma del Estado de México, Mexico City, Mexico<br>
Universidad Distrital Francisco de Miranda, Caracas, Venezuela<br>
Laboratory of Systems Genetics (LSG), Department of Computer Science, Technische Universität München, Garching, Germany<br>
Centro de Investigacion y Docencia Económicas, CIDE-UNAM, Mexico City, Mexico<br>
Department of Immunology, University of Maryland School of Medicine, Baltimore, MD, United States of America<br>
M

### Question: Is tGFBI Expression in Cancer Stromal Cells Associated with Poor Prognosis and Hematogenous Recurrence in Esophageal Squamous Cell Carcinoma?
### Final Decision: High TGFBI expression in ESCC tissues could be a powerful biomarker of poor prognosis and hematogenous recurrence. TGFBI in stromal cells might be a promising molecular target for ESCC treatment.
### Model Prediction: <|im_start|>user
Is tGFBI Expression in Cancer Stromal Cells Associated with Poor Prognosis and Hematogenous Recurrence in Esophageal Squamous Cell Carcinoma?<|im_end|>
<|im_start|>assistant
Is tGFBI Expression in Cancer Stromal Cells Associated with Poor Prognosis and Hematogenous Recurrence in Esophageal Squamous Cell Carcinoma?
assistant (tGFBI) is the name of a novel prognostic marker for cancers of unknown primary site (CUPS). We assessed the potential association between this novel prognostic marker and prognosis and hematogenous recurrence for esophageal squamous cell carcinoma (ESCC), one of the most common malignancies in the human body, and compared it to established predictors. Based on a prospective multicenter study including 159 patients with ESCC, we found that the expression of the marker in the tumor cells and surrounding stroma was significantly correlated with tumor stage, TNM, Ki67, and HER2 expression. After excluding the tumors with high risk characteristics from the results, we confirmed that the assay can correctly predict disease-free survival by evaluating a total of 834 tumors. Furthermore, we showed a close relationship between expression levels of the markers and a number of clinically relevant factors, including tumor stage and grade, which are frequently known prognostic indicators but difficult to evaluate directly.
We found a significant correlation between the expression of the tissue transglutaminase 1 (tGFBI) antigen in cancer cells and the prognosis of esophageal squamous cell carcinoma (ESCC). It is likely that the expression of the prognostic marker has an important role in ESCC as compared to conventional prognostic variables such as pathological TNM stage, the presence of lymph nodes metastasis, serum carcinoembryonic antigen level or baseline pemetrexed administration, and to evaluate the underlying disease state, but is not always associated with specific biological features. The expression status of this prognostic marker was found correlated with tumor grade, histologic subtypes, and disease-free interval, which indicates its ability to identify subsets of patients in need of adjuvant treatment according to their underlying cancer-related characteristics.
The results from this study provide useful clues about the tissue's function of tissue transglutaminase 1 in cancer cells and suggest a promising marker for diagnosing and monitoring patients with ESCC. This prognostic marker could potentially be used as an additional marker in cancer stroma and stroma, in combination with immunohistochemical markers. It may also be helpful when performing biopsies from the tumors, especially if they are small and have tumor-stroma borders or if their tumor microenvironment is complex. In our study, the expression of tGFBI in cancer cells was a more reliable predictive factor than histological factors (such as TNM stage), although the relationship was more apparent with a decrease in the number of the tumor stages. Therefore, further studies should focus on finding reliable prognostic markers that reflect better the underlying disease.
Figure 1. Representative image of the tGFBI protein
Based on the current clinical practice guidelines, prognosis remains poor among patients with ESCC despite adequate resection, with 5-year overall survival rates of approximately 30% and a 10% recurrence-free rate after surgery. The molecular basis behind these poor outcomes is largely unknown. Therefore, a large number of ongoing clinical trials are underway aiming to determine the potential mechanisms that contribute to disease progression and tumor recurrence, in addition to other factors associated with poor prognosis and recurrence in other solid tumors. Among these clinical trials, those evaluating the activity of antineoplastic drugs have identified a subset of patients who are expected to benefit from them and have improved their survival rates significantly. These results were achieved through studies using small-molecule inhibitors. To this end, we found that the expression levels of the tissue transglutaminase 1 (tGFBI) antigen were significantly higher in cancer cells and cancer-associated fibroblasts than in adjacent normal tissues or the blood vessels of the primary tumor (PT). We believe that the tissue transglutaminase 1 could be used as a novel predictive marker of cancer prognosis based on its expression in cancer cells in cancer stem-like cells, stroma, and extracellular matrix (ECM). We assessed the clinical significance of tGFBI expression in human ESCC and demonstrated that its higher expression was associated with poor prognosis

### Question: Are autoimmune features associated with chronic antibiotic-refractory pouchitis?
### Final Decision: There is marked overlap of certain immune markers in patients with pouch dysfunction, especially those with CARP. Microsomal antibody expression and elevated IgG4-positive plasma cell infiltration were independent risk factors for CARP.
### Model Prediction: <|im_start|>user
Are autoimmune features associated with chronic antibiotic-refractory pouchitis?<|im_end|>
<|im_start|>assistant
Male, 18y/o
Immunologically normal;
Chronic antibiotic-refractory pouchitis.
2016 Apr-Jun
Nature Reviews Urology
Takayama T, Yoshida M, Asaoka K, Hirose R, Ikeda S.
The role of CD4+Foxp3+ regulatory cells in the pathogenesis and outcome of ulcerative colitis. 768 Pound Freshman
Sophomore: My 2019-2020 school year at RWTH Aachen University (Germany) was very successful both on the personal as well as sporting level. On personal level, I finished first at the University Summer Tournament in Gdansk, Poland (USTGD). I also won silver medals at the University Championships (UCGW) on three occasions – at weightlifting in 2019, in the 82kg division with a lift of 204.5 kg. On the sporting side, I participated for two years in the Bundesliga (German Football Association's second tier) and represented my club team for all years up to and including my sophomore season. On this website you can find my stats from these years of competition. I have also participated several times in the national cup competition against teams from all around Germany and in one case even in the European Cup (the German national cup competition), representing my club Aalen (Liga Baden) each time with great results.
Overview 2019/2020
National Cup competition (Aalen) with team from Aalen (Germany):
Place: Top 4 of the National Cup
National Cup (2nd place):
Aalen (Germany):
Place: Top 4 of National Cup
UEC (University Eight Conference)
German Nationals (Baden):
Place: Top 3 of German Nationals (4th place in overall ranking)
World Cup (Poland):
Place: Silver Medalist (with a lift of 204.5 kg.)
IUF World Cup (Russia):
Place: Bronze Medalist (with a lift of 204.0 kg.)
The following highlights were among others achieved over the years by me:
Represented my team Aalen with all my strength in the national cup competition against teams from all across Germany with a great result every single time:
1. Place (in 2017)
2. Place (in 2018)
3. Place (in 2019)
Sporting successes of my university career:
University Champion (1x: 2018, 2x: 2019, 2x: 2020)
Fastest lift record (2019): 204.5 kg.
1st place: UCGD – Gdansk
Fastest weight for pull event (2018): 206 kg.
Top 4: UEGP – Hamburg
1st place: UEC – Hagen
Fastest weight for lift event (2020): 207 kg.
Fastest lift record (2020): 208 kg.
University Championship (2019):
1. Place (with a lift of 204.5 kg.)
2. Place (with a lift of 206 kg.)
UEGP (European Union Championships) – Hamburg (GER):
2. Place (15.5 kg category)
104 kg.
UEC (University Eight Conference) – Hagen (GER):
1. Place (800 kg. category)
UEC (University Eight Conference) – Dortmund (GER):
2. Place (800 kg. category)
UEC (University Eight Conference) – Duisburg (GER):
2. Place (800 kg. category) (with a lift of 806 kg.)
UEC (University Eight Conference) – Aachen (GER):
UEC (University Eight Conference) – Cologne (GER):
3. Place (800 kg. category) (with a lift of 806 kg.)
UEC (University Eight Conference) – Nuremberg (GER):
UEC (University Eight Conference) – Würzburg (GER):
UEC (University Eight Conference) – Magdeburg (GER):
UEC (University Eight Conference)

### Question: Does identical ATP1A3 mutation cause alternating hemiplegia of childhood and rapid-onset dystonia parkinsonism phenotypes?
### Final Decision: The discordance of these phenotypes suggests that there are other undiscovered environmental, genetic, or epigenetic factors influencing the development of alternating hemiplegia of childhood or rapid-onset dystonia parkinsonism.
### Model Prediction: <|im_start|>user
Does identical ATP1A3 mutation cause alternating hemiplegia of childhood and rapid-onset dystonia parkinsonism phenotypes?<|im_end|>
<|im_start|>assistant
does ATP1A3 mutation cause alternating hemiplegia of childhood and rapid-onset dystonia parkinsonism phenotype
Do AT12226 and ATP1A3 mutations cause hemiplegic cerebral palsy?
Is a single nucleotide polymorphism (SNP) in ATP1A3 related to risk for atypical infantile spasms?
Does ATP1A3 mutation cause ataxia-telangiectasia?
Atypical infantile spasms
Hemisomatistics
Mutations of the ATP1A3 gene and autosomal recessive congenital myasthenic syndrome
Dysfunction of the ATP1A3 channel in the brain
Hemiplegic Cerebral Palsy
Hemosaccades and dyscalculia in atypical infantile spasms
Loss of atrial natriuretic peptide in atypical infantile spasms
The role of ATP1A3 in the pathophysiology of spasticity
ATP1A3 and Parkinson's disease
Evidence of defect in atrial-to-ventricular coupling in patients with atypical infantile spasms caused by missense or nonsense mutations.
ATP1A3, ATP1A4, and cAMP/Ca2+ signaling in atypical infantile spasms and idiopathic hypersomnia-hypoxia
N-type calcium channel abnormalities associated with atypical infantile spasms.
Severe atonic seizures, paroxysmal tachycardias and cerebral aneurysm in a child with cerebral palsy
Sodium channels in motor control and the atypical infantile spasm syndromes.
Beta 1 Subunit of Sodium Channel Gene Mutation
Nature Reviews Neuroscience - ATP1A3 as a Potential RNAi Target
ATP1A3 and the cGMP-protein phosphodiesterase PDE3A
Cytosolic phosphate concentration regulates the binding of ATP1A3 to a putative PDE3A-binding motif on the cytoplasmic surface
The Role of ATP1A3 in atypical infantile spasms, sporadic idiopathic sudden hearing loss, and acoustic neuroma.
Sensory processing in atypical infantile spasms: a review
Molecular mechanisms involved in the spontaneous and sensitized burst discharges in atypical infantile spasms
Pharmacological Characterization of Neuronal Sodium-Ventricular Gradient, Channels, and Conduction at the Sensory Efferent Ganglion: In Vivo and In Vitro Modulation Studies FTC's Lina Khan to Address Net Neutrality and "Big Tech" Regulatory Issues at New America Event
In her upcoming keynote speech, Federal Trade Commission Chairwoman Lina Khan will address Internet policy, including net neutrality and the impact of the Internet on "big tech."
New America will host the 10th Annual Summit on the Future of Technology and Democracy on Thursday, March 15 from 9am – 5pm ET. Lina Khan's keynote speech will be livestreamed through the webcast portal, and you can watch the livestream by signing up here: https://newamerica.org/events/summit-on-the-future-of-technology-and-democracy/.
Speaking at the virtual summit will also be:
Keith Enright, Chair, Consumer Technology Association
Andrew Dodge, Partner, Davis Polk & Wardwell
Jason Cone, CEO, The Internet Association
Danielle Blanks, Deputy Director, Digital Policy Program, Public Knowledge
Andy Stone, Vice President, Advocacy, Advertising & Consumer Protection, Public Knowledge
Michael O'Rielly, CEO, FCC
Penny Nance, Executive Vice President, U.S. Business Group, American Council On Renewable Energy
James Grimmelmann, Professor, Northwestern University School of Law
Davis Polk will host its annual summit to examine key issues on the future of technology policy, and explore potential policy solutions to complex challenges faced today. New America is the leading think tank in Washington, DC focused on the global political, economic

### Question: Does metabolic control analysis of the Trypanosoma cruzi peroxide detoxification pathway identify tryparedoxin as a suitable drug target?
### Final Decision: These quantitative kinetic and metabolic analyses pointed out to TXN as a convenient drug target due to its low catalytic efficiency, high control on the flux of peroxide detoxification and role as provider of reducing equivalents to the two main peroxidases in the parasite.
### Model Prediction: <|im_start|>user
Does metabolic control analysis of the Trypanosoma cruzi peroxide detoxification pathway identify tryparedoxin as a suitable drug target?<|im_end|>
<|im_start|>assistant
<|im_start|>doctor
<|im_start|>student
What's the impact of the new European Union funding programme Horizon 2020 on the future of research and innovation?<|im_end|>
<|im_start|>national government
<|im_start|>private sector
<|im_start|>civil society
Which is your biggest concern when it comes to research and innovation in Italy? Which are your greatest hopes for the years ahead? (Answers will be anonymous)<|im_end|>
<|im_start|>researchers & scientists
<|im_start|>businesses
<|im_start|>policy makers
<|im_start|>society at large
<|im_start|>stakeholders in policy making
<|im_start|>citizens
Are you an expert in this field or would like to share a commentary, questionnaire, data or results? Contact us. Govt. of India Approves Additional Incentives for Small Scale Manufacturing Units under SEZs and SAMs
Posted by Rohit Jain | Aug 18, 2017 | Sector: Other, Other | 5549 views
The Government of India has approved the proposal of adding some more incentives under Section 10 of Schedule V of the Subsidiary Industries Act, 1965 for the Small Scale Manufacturing Units (SSMUs) under Special Economic Zones (SEZs), where the manufacturing units are located. A total of Rs 2,500 crore (Rs 25 billion) incentive has been given for the SSMU. This was informed by Union Finance Minister Arun Jaitley during his interaction with industry representatives at National Association of Software and Services Companies (NASSCOM) Annual Conclave 2017.
Under Section 10 of Schedule V of the Subsidiary Industries Act, 1965, a special economic zone may make provisions for the construction of units belonging to specified industries. Section 10 of this law is relevant only to SSMUs having a net book value of manufactured goods production in excess of Rs 3 lakh and a fixed asset base not exceeding Rs 1 crore in terms of previous Act. The Act provides that the value of land acquired by a State shall include its cost or such other value as it considers reasonable.
As per the Act, such units need to be built before they start their operations and the building work should commence within one year of issuance of Certificate of Entitlement under the SEZ. After completion of construction or before the commencement of manufacture or assembly, as the case may be, the unit shall obtain fresh approval from the SEZ Authority. This approval can be granted only after the construction or the unit is commissioned. The incentives provided to the SSMU by this law will be on the same lines as provided to the unit operating in the existing industrial estate where manufacturing has started or which has acquired site and constructed buildings under the PPP model but in terms of previous Act. This scheme is applicable for the units having capacity of manufacturing up to 10 lakhs/year per unit and having a total land area equal to one million square feet / unit or less.
Incentive given by Section 10 (1) of the Act is only on the first manufacture of goods but there is no provision for granting subsidy on raw materials/spare parts purchased from the market. However, in Section 13 of the Act, raw material purchases can be made out of a reserve available in any Reserve Bank of India account maintained by a banking company and not more than 5 percent of turnover (whichever is lower). This reserve can be utilized for purchase of raw materials, spares etc. It can be used by a SEZ or SEZ units registered under SEBI (Securities and Exchange Board of India) Regulations for its own operations.
The SSMU has to register as a unit in a designated centre with SEZ Authority and can start operations in that particular centre in two years as against three months earlier and thereafter every subsequent centre for which a SEZ Authority gives approval shall have to be given. Such registration must be completed at least once every five years and after that if required. In addition, the Government of India will provide an incentive equivalent to 10 percent of the total turnover and the eligibility period shall be five years. The subsidised

### Question: Is basal Flt1 tyrosine kinase activity a positive regulator of endothelial survival and vascularization during zebrafish embryogenesis?
### Final Decision: Flt1-tyrosine kinase (TK) activity contributed significantly in endothelial cells survival and vascular development during embryo angiogenesis in zebrafish by engaging PI3K/Akt pathway.
### Model Prediction: <|im_start|>user
Is basal Flt1 tyrosine kinase activity a positive regulator of endothelial survival and vascularization during zebrafish embryogenesis?<|im_end|>
<|im_start|>assistant
<|im_start|>cruiser
<|im_start|>coach
<|im_start|>lance
<|im_start|>scout
<|im_start|>shuttle
<|im_start|>sniper
<|im_start|>transporter
<|im_start|>veteran
<|im_start|>trailblazer FavoritesHistory Journal Contact Advertise with us About Us RSS Facebook Twitter
Articles by: matthew g.t. hammond
Trevor Noah says the truth about his childhood is 'a lot less funny than you think'
Daily Show star Trevor Noah says he was raised in the'most beautiful place in South Africa' but that it wasn't always all that sunny inside the family home because Mugabe was 'in the house' when they weren't around. Noah is also quick to note that while the 'hilarious' moments from his childhood were more authentic, the'real truth […]
Iowa lawmakers to consider making unborn children legal citizens
The Iowa Senate has passed legislation that would recognize an unborn human as a legal citizen. The bill would establish "Unborn Child Protection From Dismemberment Abortion Act," which is supported by pro-life groups. However, the bill is expected to face opposition from pro-choice activists who say the bill would force taxpayers to pay for procedures performed on an unborn […]
CNN analyst calls Republicans, Donald Trump supporters 'f—ing racist'
During an appearance on CNN Friday morning, Republican political commentator Chris Cilizza said there are Republicans "who hate African Americans and Hispanics and gays, and lesbians." "These are all Republican voters, some of whom are voting for President Trump," Cilizza said while referencing the president's 2016 victory. Cilizza also added that he was offended when he heard President […]
China's top economic planner vows to boost trade relations between the two countries
As tensions continue between the U.S. and China over trade issues, China's top economic planner has voiced optimistic views regarding the relationship with America. Zhao Qizhi is reportedly the head of National Development and Reform Commission. He was quoted as saying at the World Economic Forum on Wednesday that "the bilateral trade will undoubtedly continue to increase." […]
Iranian parliament speaker warns U.S.: You'd better not attack our military bases
Hossein Amir Abdollahian, Iranian Parliament Speaker warned the United States of an "extremely severe" response if the country attacks any part of Iranian territory. In a speech delivered to the National Security Council in Tehran, Amir Abdollahian said that Iran will "respond firmly" to any American provocation. In another related statement released by Iran's Foreign Ministry, Iranian President […]
Japanese government announces plans to ban sale of cigarettes on July 1st
The Japanese government is reportedly considering a plan to ban sales of cigarettes altogether or raise prices in order to reduce its addiction rates. On Thursday, Japanese Cabinet Secretary Yoshihide Suga made the announcement stating that a ban would make little sense in light of Japan's relatively high smoking prevalence rate. While a "substantial reduction" in the smoking […]
House Democrats release list of Trump impeachment witnesses they intend to call
House Democrats have announced a list of people they plan to call to testify during the House's impeachment investigation into President Trump. A summary of those individuals includes "any and all witnesses" in regard to the Ukraine scandal. According to the report, only one person will be called to the witness stand during the full House trial in Washington, D.C., […]
Energy and Commerce Committee to hold hearing on 'Farm to Market'
The House Energy & Commerce Committee has scheduled a hearing entitled 'Farm to Market.' According to Chairman Greg Walden, the hearing will explore how the Federal government can assist in rural communities. "Our rural communities are facing enormous challenges from a host of disparate national threats including the opioid epidemic, affordability crises, natural disasters and the growing […]
Suspected gunman in Virginia church massacre arrested in Texas
The suspect in last weekend's deadly shooting rampage at a Virginia Eagle Church has been

### Question: Do immunizations with hepatitis B viral antigens and a TLR7/8 agonist adjuvant induce antigen-specific immune responses in HBV-transgenic mice?
### Final Decision: Immunization with CL097-conjugated HBV-Ag reversed immune tolerance in HBV-Tg mice and induced antigen-specific immune responses. TLR7/8 agonists appear to be potent adjuvants for the induction of antigen-specific Th1 responses in an immune tolerant state.
### Model Prediction: <|im_start|>user
Do immunizations with hepatitis B viral antigens and a TLR7/8 agonist adjuvant induce antigen-specific immune responses in HBV-transgenic mice?<|im_end|>
<|im_start|>assistant
Hepatitis B virus immunoglobulin-E: T cell receptor genes from human monocyte clones<|im_start|>
<|im_end|>
Immunization of HBV transgenic mice with an adjuvanted hepatitis B vaccine to produce a protective immune response against homologous recombination vaccines<|im_start|>
<|im_end|>
Effects of antibody response and hepatitis B surface antigen on the immunopathology of chronic hepatitis B<|im_start|>
<|im_end|>
Immunity to HBsAg in vaccination, passive transfer, and transgene expression is determined by the primary immune system<|im_start|>
Hepatitis B immunogenicity: Evaluating the ability of recombinant hepatic HBsAg to cause immunosuppression<|im_start|>
Lack of effect of polyclonal antibodies to recombinant HBsAg on the immunopathological course of experimental hepatitis<|im_start|>
Immunopathology of hepatitis caused by recombinant hepatitis B surface antigen (Recom).<|im_start|>
<|im_end|>
Impact of polyclonal antibodies to recombinant hepatitis B surface antigen (Recom) on the pathophysiological outcome of experimental hepatitis<|im_start|>
<|im_end|>
Mucosal immune responses of liver after HBV exposure to inoculate the nonhuman primate (NHP)-specific HBV recombinant vaccine<|im_start|>
<|im_end|>
Hepatitis B recombinant vaccine induced mucosal immune responses in NHP that were determined using polymerase chain reaction (PCR)>|im_start|>
<|im_end|>
The safety, immunogenicity, and tolerability of an intravenous, subcutaneous, and oral recombinant hepatitis B recombinant vaccine<|im_start|>
Immunogenicity in NHP: Spleen cells from an ABO blood group-negative female NHP injected with recombinant HBV antigens produce IgG-heavy-chains<|im_start|>
HBsAg and HAV protective immunity: The influence of age on protective efficacy at different exposures<|im_start|>
Hepatitis B virus reactivated from immature foci of liver fibrosis can generate autoimmune responses.
<|im_start|>
<|im_end|>
Purification and characterisation of major anti-hepatitis B virus antibodies from an antigenically diverse group of hepatitis B surface antigen (HBsAg)-seropositive NHP
Hemagglutination inhibition testing of sera from NHP showing detectable HBsAg, and sera from NHP without evidence of current hepatitis B infection: report of results
Techniques for detecting surface antigen expression of the hepatitis B virus
Antibody Response after Vaccination With Recombinant Hepatitis B Surface Antigen (HBs Ag): A Case Report
Vaccinia virus-derived recombinant glycoproteins inducing protective humoral and cellular immune responses in hamster models.
Cleavage of HBsAg by bacterial proteases of Streptococcus pyogenes (Group A beta-hemolytic streptococci): Implications for bacterial resistance to recombinant antigens.
Antigenicity of HBsAg derived from a recombinant hemagglutinin protein of hepatitis B virus in pigs: I. Specificity studies with monoclonal antibodies and antibodies specific to pig epithelium.
Monovalent and heterologous immunization with recombinant hemagglutinin protein of hepatitis B virus from pigs induces neutralizing antibodies against hepatitis B surface antigen: implications for vaccination strategies. News > Nation
2 die at N.J. nursing home; 15 others infected
UPDATED: Fri., Sept. 4, 201

### Question: Are lobar microbleeds associated with a decline in executive functioning in older adults?
### Final Decision: Lobar microbleeds, a marker of cerebral amyloid angiopathy, are associated with an accelerated rate of executive function decline. The presence of cerebral amyloid angiopathy may be an important source of cognitive decline in aging. Future work should examine how cerebral amyloid angiopathy interacts with neurodegenerative processes, such as Alzheimer's disease.
### Model Prediction: <|im_start|>user
Are lobar microbleeds associated with a decline in executive functioning in older adults?<|im_end|>
<|im_start|>assistant
Are lobar microbleeds associated with a decline in executive functioning in older adults?
Are lobar microbleeds associated with a decline in executive functioning in older adults?
I hope the above answers your question on how to find a good research question and how to choose a question that can be useful for a dissertation proposal.
The above discussion is only about dissertations and only about dissertations from US universities. I do not know anything of the process of creating a thesis proposal elsewhere, because I have never been a student at another university or even in another country. The discussion below can thus also apply more generally.
When preparing a research proposal you should think through your question from a very detailed level up to the broadest possible, to create an answerable question, not just something that sounds interesting as a topic, but what would actually give you results. You should ask yourself: What are the most important things that I need to look into?
What would interest me most about this question? Is there anything else? Is there any other question which could help to solve the problem? And why?
After you have considered these questions you need to formulate a question with enough specificity so it will enable you to find the data needed (by finding a method suitable to your task), but still with enough breadth that you are able to understand where all the details are needed to achieve the purpose of your research. For example, when it comes to clinical research, we always try to formulate questions using a broad context to avoid misunderstanding.
How would answering my question help me?
You should ask yourself, by answering this question, what would happen to myself and/or others if my hypotheses were true? By doing this, you create a motivating goal for your research (which you can also call the "rationale" for your study).
For example, I am interested in studying dementia. This is my rationale (for myself) to have more knowledge of the disease. But then I ask myself: Why did I start this research project? As I am developing a study that will last for one year, with the data collection planned for the end of the third quarter 2014 (my thesis proposal has a year as a scope), I would like the rationale to reflect that my goal is to become more knowledgeable about this disease over time - not that I have this disease (since this will not happen, but maybe later), but instead that I will be better equipped to deal with dementia when I get it (I think the latter is less likely here, since I am still alive; it might happen, but it probably doesn't). So in this sense, I want to become an expert to be able to make better decisions on dementia when I eventually get it (as long as I don't). If this is not motivating enough for me to learn more about this disease over the course of my project, then I wouldn't do the study at all (or I would take care that I don't do my research in a way which would help my personal interest in gaining expertise); however, if my motivation and rationale are strong, then I'm willing to go into the study. It could also be that I am curious about this disease and the possibility of becoming an expert, though I feel that I won't actually accomplish my goal by knowing too much about this disease. Or perhaps I feel that knowing too little about dementia will be good for my sanity. In all cases, I would have more insight into the disease, which will lead to better clinical care (and perhaps preventative measures), which will benefit patients and society as a whole. Of course, the rationale can be used to help others get motivated (such as when I tell people that I have studied dementia - or perhaps even when they want to ask me questions about it).
Now you have formulated a rationale that may apply to you as well, hopefully giving you a starting point for thinking through a specific research question.
In order to have a research question that helps us find out the answer to our question, you first must determine what your questions ask. Here's where you need to start considering two important parts of research, which are often not clearly defined in research proposals:
What do you mean by what?
Why does it matter what?
You can have a clear answer for part one: What question do you wish to answer?
And for part two: why does it matter to what? Why is it relevant that what you are asking is important to know? For instance: Why would you really care about what you are trying to discover? Perhaps you have heard about someone in your family who is afflicted with Alzheimer's Disease. You are curious about their case in some ways but would prefer to investigate

### Question: Is self-reported physical activity in smoking pre-cessation a protective factor against relapse for all?
### Final Decision: Previous quit attempts and professional activity were positive predictors of smoking abstinence, with alcohol use disorder a negative predictor. PA was not found to be a significant predictor of smoking relapse, with only a positive interaction term seen for persons on antidepressant treatment. (Am J Addict 2014;XX:1-7).
### Model Prediction: <|im_start|>user
Is self-reported physical activity in smoking pre-cessation a protective factor against relapse for all?<|im_end|>
<|im_start|>assistant
Is self-reported physical activity in smoking cessation a protective factor against relapse for all?<|im_end|>
Are women, aged 18 and over, who smoke a protective factor against the relapse of cigarette smoking for smokers who have previously tried to quit?<|im_start|>
Are women, aged 18 and over, who smoke a protective factor against the relapse of cigarette smoking for smokers who are still using nicotine replacement therapy (NRT) to help them quit?<|im_start|>
Are women, aged 18 and over, who smoke a protective factor against the relapse of cigarette smoking for smokers who are using NRT to help them quit?<|im_start|>
Are men, aged 18 and over, who smoke a protective factor against the relapse of cigarette smoking for smokers who have never used NRT to help them quit?<|im_start|>
Are men, aged 18 and over, who smoke a protective factor against the relapse of cigarette smoking for smokers who are using NRT to help them quit?<|im_start|>
Are people with a severe mental illness a protective factor against the relapse of cigarette smoking for smokers who have never used NRT to help them quit?<|im_start|>
Are people with a severe mental illness a protective factor against the relapse of cigarette smoking for smokers who are using NRT to help them quit?<|im_start|>
Are people with a psychotic disorder a protective factor against the relapse of cigarette smoking for smokers who have never used NRT to help them quit?<|im_start|>
Are people with a psychotic disorder a protective factor against the relapse of cigarette smoking for smokers who are using NRT to help them quit?<|im_start|>
Are young people, aged 18 to 24 years old, who smoke a protective factor against the relapse of cigarette smoking for smokers who have never used NRT to help them quit?<|im_start|>
Are young people, aged 18 to 24 years old, who smoke a protective factor against the relapse of cigarette smoking for smokers who are using NRT to help them quit?<|im_start|>
Are people with a psychiatric diagnosis a protective factor against the relapse of cigarette smoking for smokers who have never used NRT to help them quit?<|im_start|>
Are people with a psychiatric diagnosis a protective factor against the relapse of cigarette smoking for smokers who are using NRT to help them quit?<|im_start|>
The relative risk for relapse for all smokers is
-3.0994165579
Whereas for those who have never used NRT it is: -1.1099374219
And finally, whereby the relative risk of relapse for people who use NRT is
-0.9035532577
Cigarette Smoking among Adults by Selected Psychological Factors
The data analysis shows that there were no significant differences between individuals who smoke and do not smoke and those who quit smoking or abstain from smoking.
Smoking is a major public health problem. According to World Health Organisation's World report on prevention of cancer in 2015, the major causes of cancer deaths globally are tobacco smoking. The global smoking prevalence was 18.4% among adults in 2012; that is almost 4 billion adults around the world. These figures show a decrease in the worldwide prevalence of cigarette smoking since the previous study by WHO. However, there has been a decrease only by about 1%. This means that almost 4 billion people have not given up smoking tobacco. A large number of these persons are still addicted to the habit of smoking.
Smokeless tobacco use increases the risk for oral cancers, head & neck cancer, bronchogenic carcinoma and chronic obstructive pulmonary disease. A recent estimate suggests 44.6 million smokeless tobacco users in India which is equivalent to about 60 percent of the total population. It is estimated that

### Question: Is breathlessness at rest the dominant presentation of patients admitted with heart failure?
### Final Decision: Many patients admitted with HF are CARBOSE. Shortness of breath at rest may be more alarming, but those who are CARBOSE have a worse prognosis, perhaps reflecting more severe right heart dysfunction. Clinical trials of hospitalized HF may inappropriately exclude patients if they focus on shortness of breath at rest rather than peripheral congestion.
### Model Prediction: <|im_start|>user
Is breathlessness at rest the dominant presentation of patients admitted with heart failure?<|im_end|>
<|im_start|>assistant
<|im_end|>
Is respiratory distress at rest the most prominent presentation in patients hospitalised for a sepsis syndrome? <|im_end|>
Is respiratory failure at rest the only major characteristic of patients with myocardial ischaemia on echocardiography? 1
Is myopathy the only clinical feature of patients presenting to the emergency department with acute myopathy, other than elevated creatine kinase levels?
Which of the following statements about respiratory tract infection are correct? 2
<|im_start|>
Myocardial perfusion abnormalities are common in patients admitted to cardiac ICUs with cardiogenic shock.
Breathlessness associated with pneumonia is more likely a manifestation of pneumothorax compared to patients with acute hypoxaemic respiratory failure. 3
Myocardial ischemia may be associated with a normal arterial carbon dioxide tension.
Assessment of hypoxic pulse oximetry requires the measurement of pulse CO2, as well as pH, bicarbonate, partial pressure of carbon dioxide and blood gases. 4
The initial diagnosis is usually established by performing invasive hemodynamic measurements (e.g. cardiac catheterization). 5
The use of invasive hemodynamic monitoring has been found to be helpful in the early identification of cardiogenic shock in patients with severe acute respiratory distress syndrome. 6
What are the key principles in assessing acutely breathless patients? 7
Determine the cause of breathlessness; this will help determine if invasive hemodynamic studies (such as arterial blood gas measurements) are needed.
Differentiate between acute respiratory distress syndrome and other causes of breathlessness such as pneumonia or infective endocarditis. 8
In cases of suspected infective endocarditis it is important to exclude the possibility of a systemic vasculitic inflammatory process. 9
Determine the cause of a sudden onset of breathlessness:
Assess the severity of the disease. In patients admitted to an ICU with myocardial ischaemia, the assessment will be restricted to the cardiac system. A patient with cardiomegaly (defined as an increase of >25% over the baseline value), acute myopericarditis, myocardial infarction and arrhythmia is considered to have an acute coronary syndrome. 10
Exclude causes that might not have a severe impact on morbidity and mortality: such as acute exacerbations of chronic obstructive lung disease, infective bronchiolitis, chronic bronchitis, asthma and pneumonias. 11
Although respiratory rate is a common measurement in most emergency departments, its interpretation should be limited and not overused. 12
A fast RR is the result of an increase in respiratory rate secondary to respiratory distress from a mycoplasmophilic infection, or from tachypnoea. This reaction is the result of increased secretion of large amounts of mucus, which causes a greater respiratory drive.
It is also common to see a RR of less than 18. The reason for this is the presence of atelectasis, a decrease in lung volume resulting from increased airway obstruction. It may not appear obvious, but air trapping should always be evaluated in order to differentiate pneumonia/asthma from mycoplasmophilic infections or acute bronchiolitis. 13
An abrupt reduction in respiratory rate (within the next hour) in the setting of fever is often seen with sepsis. This is due to vasodilation associated with fever and hypovolemic shock. It also indicates cardiogenic arrest in those who have been unconscious before admission to an intensive care unit, or in whom heart function cannot be reliably assessed using tissue Doppler imaging. 14
Acute respiratory distress syndrome is one of the leading causes of death in the ICU. The key features include acute decreased respiratory effort (due to air leakage into the alveolar space), alveolar hyperinflation and acute hypoxaemia.
All these findings will contribute towards determining the correct diagnosis of pneumonia or sepsis.
Pul

### Question: Is delayed duodenal stump blow-out following total gastrectomy for cancer : Heightened awareness for the continued presence of the surgical past in the present the key to a successful duodenal stump disruption management . A case report?
### Final Decision: Several strategies have been proposed for the successful management post-gastrectomy duodenal stump disruption however; its treatment planning is absolutely determined by the presence or not of generalized peritonitis and hemodynamic instability with hostile abdomen. In such scenario, urgent reoperation is mandatory and the damage control principle should govern the operative treatment.
### Model Prediction: <|im_start|>user
Is delayed duodenal stump blow-out following total gastrectomy for cancer : Heightened awareness for the continued presence of the surgical past in the present the key to a successful duodenal stump disruption management . A case report?<|im_end|>
<|im_start|>assistant
This research will explore what role an assistant plays in the recovery from a complex trauma or catastrophe. This research will look at the difference that a person can make by assisting with the rehabilitation, what makes some more successful than others and what may help in the recovery process to ensure they do not relapse into addictions and substance abuse. A case study will be conducted as it is more likely to give good results. It is the responsibility of the researcher/co-author to conduct a suitable clinical trial that demonstrates if there is an influence of an assistant.
What impact does an assistant have on an individual's recovery from their life threatening accident or catastrophe?
How do assistants help people through these processes?
What makes an assistant effective and which assistants have a success rate >50%.
To explore any role assistants play in their life?
To explore how an individuals success or failure impact their own rehabilitation process.
<|im_start|>
Dermatitis herpetiformis (DH)
An allergic skin condition
Skin conditions affect 6% of the population worldwide, and dermatology is one of the most common specialties practiced by general practice physicians.
<|im_end|>
Diseases of the kidney
The kidneys perform a number of critical functions within the human body: They cleanse blood by removing waste products through excretion. They filter and conserve salt from sweat by producing urine. Finally, they regulate levels of salt and water within our body fluids by controlling secretion of hormones by the adrenals. The diseases of the kidney are generally of two types: Primary, which develop before age twenty, and secondary, which occur after age twenty.
Epilepsy is a neurological disorder characterized by recurrent, unprovoked seizures occurring within seconds or minutes (rapid-onset), lasting several seconds or minutes (slow-onset), or both (febrile).
Femoral head
Femoral head refers to the ball at the top of the femur, which is also known as the head of the femur. It is made of bone called metal plating.
<|im_start|>Femoral head
<|im_end|>
Kidney Stone
A kidney stone is any solidified particle of solid calcium or oxalate crystallites found in the kidney. Most kidney stones are calcium oxalate. In general, stones are formed when calcium ions (Ca2+) in water undergo hydrolysis reactions involving the removal of protons from the crystal surface of a crystallite or of adjacent crystals, forming smaller crystals. The kidney stone is usually more than 1 millimeter in size and may be of one or more crystal phases, each of which forms by a different combination of hydrogen ions and oxalate ions, respectively, according to the ionization energies of the hydrogen and oxalate molecules and their tendency to attract oxygen to form hydroxyl cations. Crystallites are typically hexagonal and made up of repeating groups of hydroxyoxalate molecules. Because calcium ion and oxygen atoms bond strongly with carbon, the calcium and oxygen atoms that form crystallite groups together may be loosely held to a crystallite surface. Calcium oxalate mineral particles have been known to be up to 3 mm long and 1 mm wide, although typical stone formation sizes are less than 1 mm in length and width; therefore, much larger crystals may exist, but they would not be visible. Stones vary widely in size and shape; they range in color from white or brown to black. Depending on size, a kidney stone may be solid or fluid-filled.
Oral Surgery, Oral Medicine, Oral Pathology, Oral Radiology, Prosthodontics
<|im_start|>
Pathophysiology of osteoporosis is often seen in postmenopausal women. Osteopenia and osteoporosis can coexist.
Osteoperiostitis
Infections that affect the bone marrow and periosteum are called osteo­­­­per­iostiasis. Osteo­­­ per­i­ostisis is also called osteonecrosis of the jaw (ONJ).
Sinusitis is inflammation of the sinuses due to infection.
<|im_start|>Sinusitis
<|im

### Question: Are lipoprotein phospholipase A2 mass and activity associated with the diagnosis of acute brain ischemia?
### Final Decision: The results of our study do not support the early measurement of Lp-PLA2 mass or activity levels for confirming an ischemic etiology in patients experiencing minor or transient focal neurological events.
### Model Prediction: <|im_start|>user
Are lipoprotein phospholipase A2 mass and activity associated with the diagnosis of acute brain ischemia?<|im_end|>
<|im_start|>assistant
Are lipoprotein phospholipase A2 mass and activity associated with the diagnosis of acute brain ischemia?
Are lipoprotein phospholipase A2 mass and activity associated with the diagnosis of acute brain ischemia?
Are lipoprotein phospholipase A2 mass and activity associated with the diagnosis of acute brain ischemia? (2015)
Assessment of lipoproteins in aortic arch dissection
Assessment of lipoproteins in aortic arch dissection<|im_start|> 48 hours
Is it possible to assess the association between aortic arch dissection and atheroma composition based on lipid composition?
Is it possible to assess the association between aortic arch dissection and atheroma composition based on lipid composition?<|im_start|> 48 hours
Is it possible to assess the association between aortic arch dissection and atheroma composition based on lipid composition?
Is it possible to assess the association between aortic arch dissection and atheroma composition based on lipid composition?<|im_start|> 48 hours
Assessment of lipoproteins in endovascular devices
Assessment of lipoproteins in endovascular devices<|im_start|>
Assessment of lipoproteins in endovascular devices (2015)
Assessment of lipoproteins in cardiac assist devices
Assessment of lipoproteins in cardiac assist devices<|im_start|>
Assessment of lipoproteins in cardiac assist devices (2015)
Circulating lipoprotein phosphatidylcholine levels and atrial fibrillation: the PARIS II Cohort Study
Circulating lipoprotein phosphatidylcholine levels and atrial fibrillation: the PARIS II Cohort Study<|im_start|>
Circulating lipoprotein phosphatidylcholine levels and atrial fibrillation: the PARIS II Cohort Study (2015)
Changes in serum total cholesterol, low-density lipoprotein cholesterol and triglycerides in patients undergoing primary aortic valve replacement: results from the LAPROSCOPY-AOP trial
Changes in serum total cholesterol, low-density lipoprotein cholesterol and triglycerides in patients undergoing primary aortic valve replacement: results from the LAPROSCOPY-AOP trial<|im_start|>
Changes in serum total cholesterol, low-density lipoprotein cholesterol and triglycerides in patients undergoing primary aortic valve replacement: results from the LAPROSCOPY-AOP trial (2015)
Changes in serum triglyceride and cholesterol after gastric bypass surgery
Changes in serum triglyceride and cholesterol after gastric bypass surgery<|im_start|>
Changes in serum triglyceride and cholesterol after gastric bypass surgery (2016)
Changes in lipoproteins after bariatric surgery
Changes in lipoproteins after bariatric surgery<|im_start|>
Changes in lipoproteins after bariatric surgery (2016)
Changes in lipoproteins and atherosclerosis in patients with type 2 diabetes mellitus
Changes in lipoproteins and atherosclerosis in patients with type 2 diabetes mellitus<|im_start|>
Changes in lipoproteins and atherosclerosis in patients with type 2 diabetes mellitus (2015)
Changes in lipoproteins in patients with heart failure
Changes in lipoproteins in patients with heart failure<|im_start|>
Changes in lipoproteins in patients with heart failure (2015)
Evaluation of lipoprotein phosphatidylcholine composition using a combination of immunohistochemistry and liquid chromatography–mass spectrometry
Evaluation of lipoprotein phosphatidylcholine composition using a combination of immunohistochemistry and liquid chromatography–mass spectrometry<|im_start|>
Evaluation of li

### Question: Is osteoprotegerin associated with subclinical left ventricular systolic dysfunction in diabetic hypertensive patients : a speckle tracking study?
### Final Decision: Plasma OPG values could predict subclinical LV systolic dysfunction in diabetic hypertensive patients.
### Model Prediction: <|im_start|>user
Is osteoprotegerin associated with subclinical left ventricular systolic dysfunction in diabetic hypertensive patients : a speckle tracking study?<|im_end|>
<|im_start|>assistant
<|im_end|>
<|im_start|>
<|im_end|>Assistant
<|im_start|>Dias-Silva
<|im_end|>Silva-Dias-Silva
<|im_start|>Cruz
<|im_end|>Pedra-Silva
<|im_start|>Dos Santos
<|im_end|>Afonso
<|im_start|>Veloso
<|im_end|>Souza-Alves
<|im_start|>Amaro
<|im_end|>Matos
<|im_start|>Burton
<|im_end|>
<|im_start|>Oliveira
<|im_end|>Moraes
<|im_start|>Rivera
<|im_end|>Elias-Menezes
<|im_start|>Mendes
<|im_end|>Ferreira
<|im_start|>Leite
<|im_end|>Leão
<|im_start|>de Almeida
<|im_end|>Alencar
<|im_start|>de Albuquerque
<|im_end|>Costa-Neto
<|im_start|>de Andrade
<|im_end|>Figueiredo
<|im_start|>Henao
<|im_end|>Moran
<|im_start|>Nunes
<|im_end|>Torres
<|im_start|>Araújo
<|im_end|>Gouveia
<|im_start|>Dias
<|im_end|>Nogueira
<|im_start|>Jara
<|im_end|>Bacchini
<|im_start|>Oliveira-Filho
<|im_end|>Teles-Duarte
<|im_start|>Lebre
<|im_end|>Vaz-Faria
<|im_start|>Ribeiro
<|im_end|>Bruni
<|im_start|>Cortés
<|im_end|>Lima
<|im_start|>Lee
<|im_end|>Nakamura
<|im_start|>Padilla
<|im_end|>Oliveira-Netto
<|im_start|>Ramírez
<|im_end|>Shimizu
<|im_start|>Stepanovskiy
<|im_end|>Tran-Tanh
<|im_start|>Wang
<|im_end|>Yadav
<|im_start|>Yi
<|im_end|>Yokoyama
<|im_start|>Hu
<|im_end|>Peng
<|im_start|>Wen
<|im_end|>Yuan
<|im_start|>Dong
<|im_end|>Shi What I'm Reading: "How the Mind Works" by Steven Pinker
This book is about everything you thought you knew and some things you didn't.
The thing about Pinker's writing is that he uses a lot of slides as illustrations to support his points. It makes it a little slow, but I liked this method, because I could feel my brain getting new information every time we took a break from reading for five minutes or more.
I was particularly impressed with how many times Pinker referred back to the book Human Nature. I knew it was a reference point for most of what he said, but it never occurred to me just how much that book influenced him, until reading it myself. In particular, he references a chapter on the evolutionary basis for human nature, and then references another chapter on social psychology. He even goes so far as to point out when he says things are like those other people are saying--he is, after all, using their own words to make his own case.
I have a few complaints about this book. Mostly, it has some very long passages where there isn't any action; I think it would be a good companion for an episode of Futurama called "Where No Man Has Gone Before". There also aren't really any conclusions at the end; instead, Pinker spends a lot of his

### Question: Do a new model for the standardization of experimental burn wounds?
### Final Decision: This is a safe, reliable, easy to construct and use model that has the ability to produce a regular and uniform reproducible burn due to precise temperature control associated with standardized animal positioning.
### Model Prediction: <|im_start|>user
Do a new model for the standardization of experimental burn wounds?<|im_end|>
<|im_start|>assistant
<|im_end|>
<|im_start|>
If this is not done then I'm going to have to add a step for each burn: burns on one leg, another on the other leg. In addition we'd need another model for the burn on the legs that was different from the models of the burns that were on the torso and head. Each of these burns would also require a new model, such as a single cut to the torso or a partial burn to the torso and leg. As a result, each of these burns would take several models with multiple burn types to generate all of the burn data necessary in order to represent the entire set of burn data. At this point there wouldn't be any real reason to do it, and the burn models could just be represented by the burns themselves rather than having a separate burn model file.
One of my big pet peeves is the fact that every "bodypart" is given its own burn model. For instance, we already have a burn model for the torso (tbd), but the burn model for the arms, legs and hands are their own model files. What about the heads and necks? What about the heads and necks of each limb? These babies deserve their own models. A "burn model" for the "neck" should contain a single model file which contains only the burns that happen at the neck and a burn file containing all of the burns associated with the head and neck. I also think there should be burn models for the hands (held in the left hand and right hand) and feet (shoes on or off).
So what happens if we do all this extra work? When we write a burn model for each bone, each joint and muscle, each skin, all of which have their own separate burn models for each individual burn type that occurs during a burn injury? If you look through the files for the body parts (torso, arms/legs, heads/neck/backs, hands), you will see hundreds of burn models per part. If this burn modeling process becomes cumbersome then a lot of our other burn models are going to become very complicated and very unwieldy to read and use in code that performs any sort of burn research.
Also, consider the burn injury itself. Burn injuries come in many forms and each form has its own unique set of burn-induced wound characteristics. All these unique forms can be represented by their own burn models:
•	burns on 2 out of 4 limbs
•	burns on the hands and face (12 different combinations of injury patterns)
•	burns on the torso (24 different combinations of injury patterns)
•	burns on the body (25 different combination of burn patterns)
Now consider that if someone was trying to build a burn model program that would allow you to perform burn injury-specific simulations and then compare the results to the simulation results generated by someone else. Imagine the effort it would take to write those burn injury-specific burn models (and make sure that the burn model generator itself had been updated appropriately in such cases). This means that if the burn model generation code was to change from time to time then any new code would almost certainly break.
Now imagine that instead of changing the models once in a while we had to create hundreds of burn models, each unique to some kind of burn-induced burn injury (and the various injury types that can be caused by burning, such as scarring, infection, and tissue damage). How difficult is it to read, understand, modify and reuse all of the burn models created for each and every one of these different burn injuries? How easy is it to develop code that will allow us to simulate various burn injuries? We would have thousands upon thousands of burn models to deal with.
For the record, I don't know if this problem is really all that bad. It might seem intimidating now when we look at how much more complex and complicated the burn models for each burn injury might be compared to the burn models used currently. In fact, I wonder whether we would actually find ourselves writing code to generate these burn models after all. But it appears to me that the amount of effort that goes into doing everything else in a burn modeling project is probably greater than the amount of effort it takes to write code to generate and maintain these models, even if they are far more complex. The problem isn't that simple as it seems – maybe it needs to be approached differently…
What Do They Mean By "Burn Model"?
On March 13th, 2007 the Fire Protection Research Foundation (FPRF) published the following statement regarding the use of burn modeling:
The FPRF recognizes that the use

### Question: Does circulating atrial natriuretic peptide genetic association study identify a novel gene cluster associated with stroke in whites?
### Final Decision: This is the first large-scale genetic association study of circulating NT-proANP levels performed with replication and functional assessment that identified genetic variants in the MTHFR-CLCN6-NPPA-NPPB cluster to be significantly associated with NT-proANP levels. The clinical significance of this variation is related to lower NT-proANP levels, higher blood pressures, and an increased risk of stroke in the general community.
### Model Prediction: <|im_start|>user
Does circulating atrial natriuretic peptide genetic association study identify a novel gene cluster associated with stroke in whites?<|im_end|>
<|im_start|>assistant
<|im_end|>
Evaluation of a prognostic score for mortality and cardiovascular events in patients discharged from hospital after acute myocardial infarction: a prospective cohort study<|im_start|>
A study of the natural history of carotid artery disease: results from the Multi-Prospective Carotid Atherosclerosis Prognosis Investigator Group (MAPIG)<|im_start|>
Associations between coronary artery calcium score, carotid intima media thickness, or total cholesterol and risk of myocardial infarction among older adults without known heart disease: the Third National Health and Nutrition Examination Survey
Stroke 38(5):1097–1102, 2007 May
A multivariable predictor model to predict stroke recurrence after the first ischemic stroke: data from the American Heart Association Stroke Council, Interdisciplinary Working Group on Stroke Prevention, and Stroke Nursing Committee
Prevalence of and risk factors for carotid atherosclerotic plaque reduction: a population-based cross sectional study
American Journal of Cardiology 104(1):3–6, 2009 Mar
Risk factors and their relationship with coronary calcium scores in white and black individuals: the Lifestyle Initiative Study
Am J Epidemiol 167(8):875–883, 2008 Aug
Association of serum nerve growth factor levels and apolipoprotein B with incident major adverse cardiac events following an acute ST-elevation myocardial infarction: results from the PURE trial
JAMA - Journal of the American Medical Association 309(3):373–379, 2013 Feb
Serum nerve growth factor and myocardial fibrosis in the carotid artery disease and mortality study
Diagnostic performance of carotid IMT and carotid plaques in predicting 10-year cardiovascular disease risk
JAMA - Journal of the American Medical Association 310(4):467–474, 2013 Jan 24
Serum nerve growth factor as a predictor of future coronary events: the Multi-Centre Arrhythmia Strategies in Europe (MASE) Investigators Collaboration
JACC: CardioVascular Imaging 3(5):522–530, 2010 Oct
Coronary CT angiography in the prediction of adverse clinical outcome in patients with recent-onset stable angina and prior myocardial infarction: insights from the Multi-Centre Angina Investigators Collaboration and the ProSCOURT CAPS Investigators
Circulation 123(25):2777–2785, 2011 Nov
Coronary CT angiography for evaluation of risk stratification and management of patients with previous myocardial infarction
P. Epidemiology 21(6):704–712, 2010 Dec
Effectiveness and cost-effectiveness of non-invasive strategies in secondary prevention of cardiovascular diseases with atrial fibrillation in a real-world setting
J Am Coll Cardiol - Journal of the American College of Cardiology 58(5):389–396, 2011 Jul 5
Carotid intima-media thickness and its association with adverse outcomes in the community: the Atherosclerosis Risk in Communities (ARIC) Study
N Engl J Med 354(10):982–993, 2006 Jun 29
Prediction of death by carotid atherosclerosis in patients with ischemic stroke
Neurology 67(17):1527–1534, 2006 Sep 19
The use of carotid IMT and carotid intima-media thickness measurements for early diagnosis of ischemic heart disease: results from the Coronary Artery Calcium Score Trial (CATCH)
J Am Coll Cardiol Intv 7(1):103–112, 2014

### Question: Do whole-genome sequencing and epidemiological analysis provide evidence for cross-transmission of mycobacterium abscessus in a cohort of pediatric cystic fibrosis patients?
### Final Decision: We have not demonstrated cross-transmission of M. abscessus within our hospital, except between 1 sibling pair. Alternative routes of acquisition of M. abscessus infection, in particular the environment, require further investigation.
### Model Prediction: <|im_start|>user
Do whole-genome sequencing and epidemiological analysis provide evidence for cross-transmission of mycobacterium abscessus in a cohort of pediatric cystic fibrosis patients?<|im_end|>
<|im_start|>assistant
<|im_end|>
"The results of whole-genome sequencing indicate that mycobacterium abscessus, a rare pathogen with potentially severe consequences for people with respiratory failure, was widespread among people with cystic fibrosis (CF), regardless of age or exposure. A number of persons with CF harbored the genetic variant rs5301966A/G within the mycobacterium abscessus nuclear large subunit rRNA gene 16S rRNA-H, a marker known to increase risk for lung tissue destruction in cystic fibrosis. In addition, we observe evidence that whole-genome sequencing identifies M. abscessus at a very low frequency in 24 CF lung specimens from individuals without a history of travel to high transmission regions."<|im_start|>
"To our knowledge, this is the first report of such low prevalence of M. abscessus in a non-HIV population. The very high rate of M. abscessus within CF lung samples suggests that, even though infections with this species are extremely rare, cross-infection between individuals might occur."<|im_end|> The Migrationist
Advice for writers of historical fiction about migration.
About The Migrationist
Global Migrant Reads
The Migrationist's Best of 2019: Top posts
Tag Archives: European Union
Fleeing persecution: A look at European Union policy towards refugees fleeing war and instability in Syria, Libya, North Africa and Afghanistan
Today, millions of men, women and children in the Middle East, Europe, Asia, Africa, and South America – including hundreds of thousands of those fleeing the war in Syria – are at grave risk of death or forcible return as the countries they have fled become increasingly unstable. For the European Union, the migration crisis, caused by the lack of a solution to the civil wars raging on its southern borders, has been the largest in the organization's history.
At the same time, Europe – unlike other nations like Turkey, Pakistan, Bangladesh and Ethiopia — continues to refuse to accept any Syrian refugees who arrive on EU territory despite the EU's obligations under international law to do so. In September 2016 alone, the number of people arriving on EU shores through irregular means reached an all-time record of 82,670, the majority of whom were refugees from Syria. While only a fraction of these refugees are allowed to stay on EU soil due to EU laws and regulations, many others – with the hope of eventually reaching a safe haven on Europe's shores – make their way there illegally. The situation has become so dire that the European Parliament passed a resolution calling on the EU to take "further action to ensure a safe and dignified return of all people forcibly displaced," and is calling upon the Council to "work out a more effective legal framework." Yet despite the dire straits in which Europe finds itself, the EU remains divided over how best to address its increasing humanitarian crisis.
It is important to understand the complex relationship between Europe, Syria and the people on the move – and not least because the European Union's efforts to tackle the refugee crisis will play a role in future global security, and, should the EU's current leadership not be replaced by the people of Europe themselves, may well determine whether Europe will be able to retain its political standing when the dust finally settles. Here are some important articles I've written related to the refugee crisis. Please note that the Migrationist does not publish the articles below. To comment on them please visit the original source.
From refugees to 'foreigners': What Syrians want to be told by the EU, New York Times, June 12, 2015
Germany's Muddled Refugee Policy, Der Spiegel, August 15, 2015
European Union: The Refugee Crisis as a Test for Multilateralism, Center for Global Development, July 2015
The Syrian refugee crisis: Where to start when there's so much confusion?, Deutsche Welle, October 3, 2015
Europe must stop giving in to Turkey's demands on migrants, Financial Times, May 5, 2016
What EU leaders need to know before visiting Greece on the refugee front line, European Sting, December 1, 2015
EU's lack of coordination makes dealing with refugee
### Question:
"""

# Extract Final Decisions and Model Predictions
final_decisions = re.findall(r'### Final Decision: (.+)', log_data)
# model_predictions = re.findall(r'### Model Prediction: <\|im_start\|>assistant\s*(.*?)\n### Question:', log_data, re.DOTALL)

model_predictions = re.findall(r'<\|im_start\|>assistant.*?(.*?)\n### Question:', log_data, re.DOTALL)
# Strip unwanted whitespace or newline characters
model_predictions = [pred.strip() for pred in model_predictions]

# Output the lists
print("----------------------Final Decisions------------------------")
print("Final Decisions:", final_decisions)
print("----------------------Model Predictions------------------------")
print("Model Predictions:", model_predictions)
print(("----------------------Match_status------------------------"))

# Add print statements to check the number of elements in each list
print(f"Number of Final Decisions: {len(final_decisions)}")
print(f"Number of Model Predictions: {len(model_predictions)}")

P, R, F1 = bert_score.score(model_predictions, final_decisions, lang='en', verbose=True)

# Print the results
print(f"Precision: {P.mean().item():.3f}")
print(f"Recall: {R.mean().item():.3f}")
print(f"F1 Score: {F1.mean().item():.3f}")


