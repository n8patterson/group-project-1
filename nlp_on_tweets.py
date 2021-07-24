import fasttext
import numpy as np
import spacy
from scipy.spatial import distance

# a statistical model we will use to split docs into sentences
spacy_model = spacy.cli.download("en_core_web_sm")
sentencizer = spacy.load('en_core_web_sm')

# a 700-parameter sentence-embeddings NLP model trained on Pubmed biomedical data (20+ GB!)
# https://github.com/ncbi-nlp/BioSentVec/wiki
model = fasttext.load_model(
    '/Users/michael/fintech/group_project_1/group-project-1/BioSentVec_PubMed_MIMICIII-bigram_d700.bin')

emb = model.get_sentence_vector("once upon a time .")
# embs = model.predict("one man set out to rule the world")

company_profiles = {
    "NTLA": "Intellia Therapeutics, Inc., a genome editing company, focuses on the development of therapeutics. "
            "It utilizes a biological tool known as the Clustered, Regularly Interspaced Short Palindromic "
            "Repeats/CRISPR associated 9 (CRISPR/Cas9) system. The company's in vivo programs include NTLA-2001,"
            "which is in Phase 1 clinical trial for the treatment of transthyretin amyloidosis; and NTLA-2002 for "
            "the treatment of hereditary angioedema, as well as other liver-focused programs comprising hemophilia "
            "A and hemophilia B, hyperoxaluria Type 1, and alpha-1 antitrypsin deficiency. Its ex vivo pipeline "
            "includes NTLA-5001 for the treatment of acute myeloid leukemia; and proprietary programs focused on "
            "developing engineered cell therapies to treat various oncological and autoimmune disorders. Intellia "
            "Therapeutics, Inc. has license and collaboration agreements with Novartis Institutes for BioMedical "
            "Research, Inc. to engineer hematopoietic stem cells for the treatment of sickle cell disease; "
            "Regeneron Pharmaceuticals, Inc. to co-develop potential products for the treatment of hemophilia A "
            "and hemophilia B; and Ospedale San Raffaele. The company was formerly known as AZRN, "
            "Inc. and changed its name to Intellia Therapeutics, Inc. in July 2014. Intellia Therapeutics, "
            "Inc. was incorporated in 2014 and is headquartered in Cambridge, Massachusetts.",
    "REGN": "Regeneron Pharmaceuticals, Inc. discovers, invents, develops, manufactures, and commercializes medicines "
            "for treating various medical conditions worldwide. The company's products include EYLEA injection to "
            "treatwet age-related macular degeneration and diabetic macular edema; myopic choroidal "
            "neovascularization; and diabetic retinopathy, as well as macular edema following retinal vein occlusion, "
            "including macular edema following central retinal vein occlusion and macular edema following branch "
            "retinal vein occlusion. It also provides Dupixent injection to treat atopic dermatitis in adults, "
            "and asthma in adults and adolescents; Praluent injection for heterozygous familial hypercholesterolemia "
            "or clinical atherosclerotic cardiovascular disease in adults; and Kevzara solution for subcutaneous "
            "injection for treating rheumatoid arthritis in adults. In addition, the company offers Libtayo injection "
            "to treat metastatic or locally advanced cutaneous squamous cell carcinoma; ARCALYST injection for "
            "cryopyrin-associated periodic syndromes, including familial cold auto-inflammatory syndrome and "
            "muckle-wells syndrome; and ZALTRAP injection for intravenous infusion to treat metastatic colorectal "
            "cancer. Further, it offers Inmazeb injection for infection caused by Zaire ebolavirus; and develops "
            "product candidates for treating patients with eye, allergic and inflammatory, cancer, cardiovascular and "
            "metabolic, pain, infectious, and other diseases. The company has collaboration and license agreements "
            "with Sanofi; Bayer; Teva Pharmaceutical Industries Ltd.; Mitsubishi Tanabe Pharma Corporation; Alnylam "
            "Pharmaceuticals, Inc.; Roche Pharmaceuticals; and Kiniksa Pharmaceuticals, Ltd., as well as has an "
            "agreement with the U.S. Department of Health and Human Services. It has collaborations with Zai Lab "
            "Limited; Intellia Therapeutics, Inc.; and Biomedical Advanced Research Development Authority. Regeneron "
            "Pharmaceuticals, Inc. was founded in 1988 and is headquartered in Tarrytown, New York.",
    "CRSP": "CRISPR Therapeutics AG, a gene editing company, focuses on developing transformative gene-based "
            "medicines for serious human diseases. The company develops its products using Clustered Regularly "
            "Interspaced Short Palindromic Repeats (CRISPR)/CRISPR-associated protein 9 (Cas9), a gene editing "
            "technology that allows for precise directed changes to genomic DNA. It has a portfolio of therapeutic "
            "programs in a range of disease areas, including hemoglobinopathies, oncology, regenerative medicine, "
            "and rare diseases. The company's lead product candidate is CTX001, an ex vivo CRISPR gene-edited therapy "
            "for treating patients suffering from transfusion-dependent beta thalassemia or severe sickle cell "
            "disease in which a patient's hematopoietic stem cells are engineered to produce high levels of fetal "
            "hemoglobin in red blood cells. It also develops CTX110, a donor-derived gene-edited allogeneic CAR-T "
            "therapy targeting cluster of differentiation 19 positive malignancies; allogeneic CAR-T programs "
            "comprising CTX120 targeting B-cell maturation antigen for the treatment of relapsed or refractory "
            "multiple myeloma; and CTX130 for the treatment of solid tumors and hematologic malignancies. It develops "
            "regenerative medicine programs in diabetes; and in vivo and other genetic disease programs to treat "
            "glycogen storage disease Ia, Duchenne muscular dystrophy, myotonic dystrophy type 1, and cystic "
            "fibrosis. The company has strategic partnerships with Bayer Healthcare LLC, Vertex Pharmaceuticals "
            "Incorporated, ViaCyte, Inc., Nkarta, Inc., and Capsida Biotherapeutics. The company was formerly known "
            "as Inception Genomics AG and changed its name to CRISPR Therapeutics AG in April 2014. CRISPR "
            "Therapeutics AG was incorporated in 2013 and is headquartered in Zug, Switzerland.",
    "EDIT": "Editas Medicine, Inc., a clinical stage genome editing company, focuses on developing transformative "
            "genomic medicines to treat a range of serious diseases. It develops a proprietary genome editing "
            "platform based on CRISPR technology to target genetically addressable diseases and therapeutic areas. "
            "The company develops EDIT-101, which is in Phase 1/2 clinical trial for Leber Congenital Amaurosis type "
            "10, a genetic form of vision loss that leads to blindness in childhood. It also develops EDIT-102 for "
            "the treatment of Usher Syndrome 2A, which is a form of retinitis pigmentosa that also includes hearing "
            "loss; autosomal dominant retinitis pigmentosa 4, a progressive form of retinal degeneration; and "
            "EDIT-301 to treat sickle cell disease and beta-thalassemia. In addition, the company is developing "
            "gene-edited Natural Killer cell medicines to treat solid tumors; alpha-beta T cells for multiple "
            "cancers; and gamma delta T cell therapies to treat cancer, as well as has a early discovery program to "
            "develop a therapy to treat a neurological disease. It has a research collaboration with Juno "
            "Therapeutics, Inc. to develop engineered T cells for cancer; strategic alliance and option agreement "
            "with Allergan Pharmaceuticals International Limited to discover, develop, and commercialize new gene "
            "editing medicines for a range of ocular disorders; and research collaboration with Asklepios "
            "BioPharmaceutical, Inc. to develop a therapy to treat a neurological disease, as well as research "
            "collaboration with AskBio and collaboration with m BlueRock Therapeutics LP. The company was formerly "
            "known as Gengine, Inc. and changed its name to Editas Medicine, Inc. in November 2013. Editas Medicine, "
            "Inc. was incorporated in 2013 and is headquartered in Cambridge, Massachusetts.",
    "BLUE": "bluebird bio, Inc., a biotechnology company, researches, develops, and commercializes transformative "
            "gene therapies for severe genetic diseases and cancer. Its product candidates for severe genetic "
            "diseases include betibeglogene autotemcel for the treatment of transfusion-dependent Ã-thalassemia; "
            "LentiGlobin for the treatment of sickle cell disease; and elivaldogene autotemcel to treat cerebral "
            "adrenoleukodystrophy. The company's product candidates in oncology include Idecabtagene vicleucel and "
            "bb21217, which are chimeric antigen receptor T (CAR T) cell product candidates for the treatment of "
            "multiple myeloma. It has collaboration and license agreements with Bristol-Myers Squibb, "
            "Regeneron Pharmaceuticals, Inc., Novartis Pharma AG, Orchard Therapeutics Limited, Medigene AG, "
            "Novo Nordisk A/S, Forty Seven, Inc., Gritstone Oncology, Inc., Magenta Therapeutics, Inc., the Seattle "
            "Children's Research Institute, University of North Carolina, and the Fred Hutchinson Cancer Research "
            "Center. The company was formerly known as Genetix Pharmaceuticals, Inc., and changed its name to "
            "bluebird bio, Inc. in September 2010. bluebird bio, Inc. was incorporated in 1992 and is headquartered "
            "in Cambridge, Massachusetts."
}


def get_similarity(tweet, document_embedding):
    tweet_sentences = [t.text for t in sentencizer(tweet).sents]
    tweet_embedding = np.mean(
        [model.get_sentence_vector(s) for s in tweet_sentences], axis=0)
    return 1 - distance.cosine(tweet_embedding, document_embedding)


if __name__ == "__main__":
    # first, extract sentences and infer+store their embeddings for each company
    sentence_embeddings = {
        symbol: [model.get_sentence_vector(s.text) for s in sentencizer(company_blurb).sents]
        for symbol, company_blurb in company_profiles.items()
    }

    # to get document embeddings, we take the mean of the sentence embeddings
    blurb_embeddings = {
        symbol: np.mean(np.array([s for s in blurb_sentences]), axis=0)
        for symbol, blurb_sentences in sentence_embeddings.items()
    }

    for tweet in ['this is a sentence about biotechnology',
                  'I used crispr on my mosquitos',
                  'the children need their therapeutic cancer treatment']:
        print(get_similarity(tweet, blurb_embeddings['EDIT']))
