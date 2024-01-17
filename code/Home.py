import streamlit as st

st.set_page_config(layout="wide")

#---------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neat Decoration</title>
    <style>
        body {
            background-color: #f7f7f7;
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .decorative-box {
            text-align: center;
            padding: 20px;
            border: 2px solid #3498db;
            border-radius: 10px;
            background-color: #ecf0f1;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #3498db;
        }
    </style>
</head>
<body>
    <div class="decorative-box">
        <h1>WELCOME TO COVID-19 ANALYSIS</h1>
    </div>
</body>
</html>
""",unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------------------------

st.title("COVID-19 Overview")

st.markdown("""
    <p style='font-size:20px; line-height:1.6; text-align:justify;'>
    The COVID-19 pandemic, caused by the novel coronavirus SARS-CoV-2, emerged in late 2019 in Wuhan, China, and quickly spread globally. Characterized by respiratory symptoms, it primarily spreads through respiratory droplets when an infected person coughs or sneezes. The virus can also spread by touching surfaces contaminated with the virus and then touching the face. COVID-19 presents a spectrum of symptoms, from mild respiratory issues to severe pneumonia, and may lead to death, particularly in vulnerable populations.
    </p>
    <p style='font-size:20px; line-height:1.6; text-align:justify;'>
    Governments worldwide implemented various measures to curb the spread, including lockdowns, social distancing, and mask mandates. The pandemic's impact extends beyond health, affecting economies, education, and mental health. The scientific community collaborated to develop vaccines at an unprecedented pace, with several vaccines receiving emergency use authorization or approval. Vaccination campaigns aimed to achieve herd immunity and curb the virus's impact.
    </p>
    <p style='font-size:20px; line-height:1.6; text-align:justify;'>
    The virus's variants posed challenges, potentially affecting transmissibility and vaccine efficacy. Global efforts to enhance surveillance, research, and international cooperation aimed to address these challenges. The pandemic underscored the importance of public health infrastructure, highlighting disparities in healthcare access and the need for global solidarity.
    </p>
    <p style='font-size:20px; line-height:1.6; text-align:justify;'>
    Ongoing research explores long-term effects (post-acute sequelae) of COVID-19, impacting survivors' health even after recovery. As societies adapt to the 'new normal,' lessons learned from the pandemic inform future preparedness against emerging infectious diseases. The COVID-19 experience prompted advancements in telemedicine, vaccine technology, and public health strategies.
    </p>
    <p style='font-size:20px; line-height:1.6; text-align:justify;'>
    In conclusion, the COVID-19 pandemic has been a transformative global event, testing societal resilience, healthcare systems, and international cooperation. While progress has been made with vaccinations and treatments, the lasting effects of the pandemic will continue to shape public health, policy, and research in the years to come.
    </p>
    """, unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------------------------

st.title("Starting of COVID-19")

st.markdown("""
    <p style='font-size:20px; line-height:1.6; text-align:justify;'>
    COVID-19, caused by the novel coronavirus SARS-CoV-2, originated in late 2019 in Wuhan, China. The virus is believed to have originated in a wet market in Wuhan, with the initial cases linked to the seafood and live animal market. The World Health Organization (WHO) declared it a Public Health Emergency of International Concern on January 30, 2020, and later declared it a pandemic on March 11, 2020, as the virus rapidly spread globally.
    </p>
    """, unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------------------------

st.title("Ongoing Status of COVID-19")

st.markdown("""
    <p style='font-size:20px; line-height:1.6; text-align:justify;'>
    As of the latest information, the COVID-19 pandemic is still ongoing. Various countries have implemented measures such as vaccination campaigns, social distancing, and mask mandates to control the spread of the virus. Efforts are being made globally to achieve herd immunity through vaccination. The situation is dynamic, and ongoing research and public health measures continue to be essential in managing and eventually ending the pandemic.
    </p>
    """, unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------------------------

st.title("Precautions")

st.subheader("General Precautions")
st.markdown("""
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Vaccination:</strong> Stay informed about COVID-19 vaccines and get vaccinated when eligible.</li>
    
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Hygiene Practices:</strong>
        <ul>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Hand Hygiene:</strong> Wash hands frequently with soap and water for at least 20 seconds.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Hand Sanitizers:</strong> Use hand sanitizers with at least 60% alcohol.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Avoid Touching Face:</strong> Avoid touching eyes, nose, and mouth with unwashed hands.</li>
        </ul>
    </li>
    
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Face Coverings:</strong> Wear a mask that covers the nose and mouth, especially in crowded or indoor settings.</li>
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Physical Distancing:</strong> Maintain a safe distance from individuals who are not part of your household.</li>
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Respiratory Hygiene:</strong> Cover your mouth and nose with a tissue or your elbow when coughing or sneezing.</li>
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Cleaning and Disinfection:</strong> Regularly clean and disinfect frequently-touched surfaces.</li>
    <li style='font-size:20px; line-height:1.6; text-align:justify;' ><strong style="font-weight: bold;">Avoid Close Contact:</strong>
        <ul>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'>Avoid close contact with individuals who are sick.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'>Stay home if you are feeling unwell.</li>
        </ul>
    </li>
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Ventilation:</strong> Ensure proper ventilation in indoor spaces by opening windows and doors.</li>
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Stay Informed:</strong> Stay updated on the latest information and guidelines from health authorities.</li>
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Travel Precautions:</strong> Follow travel advisories and guidelines issued by health authorities.</li>
    
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.subheader("Individual Health Monitoring")

st.markdown("""
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Monitor Symptoms:</strong> Monitor yourself for symptoms of COVID-19, such as fever, cough, and difficulty breathing.</li>
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Seek Medical Attention:</strong> Seek medical attention if you develop symptoms, especially if they worsen.</li>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.subheader("Community Measures")

st.markdown("""
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Community Engagement:</strong> Support community efforts to control the spread of the virus.</li>
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Follow Guidelines:</strong> Follow guidelines for testing, contact tracing, and quarantine measures.</li>
    """, unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------------------------

st.title("Vaccines")
st.markdown("""
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Pfizer-BioNTech (Comirnaty):</strong>
      <ul>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Developed by Pfizer, Inc., and BioNTech SE.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Utilizes messenger RNA (mRNA) technology.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Demonstrated high efficacy in clinical trials, particularly in preventing severe illness.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Administered as a two-dose series, spaced a few weeks apart.</li>
      </ul>
    </li>

    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Moderna (Spikevax):</strong>
      <ul>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Developed by Moderna, Inc.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Also utilizes mRNA technology.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Demonstrated high efficacy in preventing COVID-19 in clinical trials.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Administered as a two-dose series, spaced a few weeks apart.</li>
      </ul>
    </li>

    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Johnson & Johnson's Janssen:</strong>
      <ul>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Developed by Janssen Pharmaceuticals Companies, a subsidiary of Johnson & Johnson.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Utilizes a viral vector platform.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Administered as a single-dose vaccine.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Demonstrated efficacy in preventing severe illness.</li>
      </ul>
    </li>

    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">AstraZeneca-Oxford (Vaxzevria):</strong>
      <ul>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Developed by AstraZeneca in collaboration with the University of Oxford.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Utilizes a viral vector platform.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Administered as a two-dose series, with varying intervals between doses.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Demonstrated efficacy against severe disease in clinical trials.</li>
      </ul>
    </li>

    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Sinopharm (BBIBP-CorV):</strong>
      <ul>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Developed by China National Pharmaceutical Group (Sinopharm).</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Inactivated virus vaccine.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Administered as a two-dose series.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Used in several countries and demonstrated effectiveness in preventing severe illness.</li>
      </ul>
    </li>

    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Sinovac (CoronaVac):</strong>
      <ul>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Developed by Sinovac Biotech.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Inactivated virus vaccine.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Administered as a two-dose series.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Deployed in various countries and demonstrated efficacy against symptomatic COVID-19.</li>
      </ul>
    </li>

    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Sputnik V:</strong>
      <ul>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Developed by the Gamaleya Research Institute of Epidemiology and Microbiology in Russia.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Utilizes a viral vector platform.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Administered as a two-dose series.</li>
        <li style='font-size:20px; line-height:1.6; text-align:justify;'>Demonstrated efficacy in preventing COVID-19 in clinical trials.</li>
      </ul>
    </li>
    
    """, unsafe_allow_html=True)


st.subheader("Commanly Used vaccines")
st.markdown("""
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Covaxin:</strong>
        <ul>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Developer:</strong> Covaxin is developed by Bharat Biotech, an Indian biotechnology company, in collaboration with the Indian Council of Medical Research (ICMR).</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Technology: </strong> Covaxin is an inactivated virus vaccine. It is created by using inactivated or killed SARS-CoV-2 virus particles.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Dosage: </strong> It is typically administered as a two-dose series with an interval of four to six weeks between doses.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Authorization: </strong> Covaxin received emergency use authorization in India in early 2021.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Usage: </strong> Widely used in India as part of the country's vaccination campaign.</li>
        </ul>
    </li>
    
    <li style='font-size:20px; line-height:1.6; text-align:justify;' ><strong style="font-weight: bold;">Covishield:</strong>
        <ul>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Developer:</strong> Covishield is the Indian version of the Oxford-AstraZeneca vaccine, manufactured by the Serum Institute of India (SII) under license from AstraZeneca.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Technology: </strong> Covishield is a viral vector vaccine. It uses a weakened version of a common cold virus (adenovirus) that infects chimpanzees and has been modified to carry the genetic material of the SARS-CoV-2 spike protein.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Dosage: </strong> Administered as a two-dose series, with an interval of four to twelve weeks between doses.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Authorization: </strong> Covishield received emergency use authorization in India and has been authorized for use in various countries.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Usage: </strong> Deployed in numerous countries worldwide through the COVAX initiative and independently procured by various nations.</li> 
        </ul>
    </li>
    
    """, unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------------------------

st.title("Vaccination Strategies")

st.markdown("""
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Vaccination Strategies:</strong>
        <ul>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Vaccine Development:</strong> The global effort to combat COVID-19 included the rapid development of vaccines using various technologies such as mRNA, viral vectors, and inactivated viruses.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Emergency Use Authorization:</strong> Regulatory agencies worldwide granted Emergency Use Authorization to several COVID-19 vaccines after rigorous testing and evaluation of safety and efficacy.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Global Vaccination Campaigns:</strong> Countries initiated mass vaccination campaigns, prioritizing frontline workers, vulnerable populations, and specific age groups to curb the spread of the virus.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Vaccine Distribution Challenges:</strong> Challenges in vaccine distribution included logistical hurdles, cold chain requirements, and equitable access, especially in low-income countries.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Booster Doses:</strong> Some countries implemented booster dose strategies to enhance immunity and address concerns about waning vaccine effectiveness against emerging variants.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Vaccine Hesitancy:</strong> Efforts were made to address vaccine hesitancy through public awareness campaigns, education, and transparent communication about vaccine safety and efficacy.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Global Vaccine Equity:</strong> International organizations and initiatives worked toward achieving global vaccine equity, ensuring fair access to vaccines for all countries, regardless of income levels.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Monitoring Vaccine Effectiveness:</strong> Ongoing surveillance and studies were conducted to monitor the long-term effectiveness of vaccines, assess their impact on reducing severe disease and hospitalization, and adapt vaccination strategies accordingly.</li>
        </ul>
    </li>

    """, unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------------------------
st.title("Testing Procedures")

st.markdown("""
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">COVID-19 Testing Procedures:</strong>
        <ul>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">PCR Testing:</strong> Polymerase Chain Reaction (PCR) testing was widely adopted for the detection of COVID-19. This diagnostic method involves the amplification of viral genetic material, providing highly accurate results and identifying active infections.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Antigen Testing:</strong> Rapid Antigen testing emerged as a quick and accessible method for detecting specific viral proteins. While less sensitive than PCR, antigen tests offered rapid results, making them valuable for screening in various settings.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Serological Tests:</strong> Serological or antibody tests were utilized to detect the presence of antibodies in an individual's blood, indicating a past infection or immune response. These tests played a role in assessing population-level immunity and vaccine effectiveness.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Nasal Swab Collection:</strong> For PCR and antigen tests, nasal swabs were commonly used to collect respiratory specimens. Swabs were inserted into the nostrils to collect samples from the nasal cavity, allowing for the detection of the virus.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Drive-Through Testing:</strong> Drive-through testing sites were established to enhance accessibility and safety. Individuals could remain in their vehicles while healthcare professionals administered tests, minimizing contact and facilitating mass testing efforts.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Testing Centers:</strong> Dedicated testing centers, both mobile and stationary, were set up globally to accommodate large-scale testing. These centers followed strict protocols to ensure accurate sample collection and timely reporting of results.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Home Testing Kits:</strong> The availability of home testing kits allowed individuals to self-administer certain tests, providing convenience and reducing the burden on testing infrastructure. Results could be reported remotely, contributing to timely surveillance efforts.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Testing Criteria:</strong> Testing criteria evolved based on public health guidelines, with priorities given to symptomatic individuals, close contacts of confirmed cases, and individuals in high-risk settings. As the situation progressed, expanded testing criteria contributed to a more comprehensive understanding of the virus's spread.</li>
        </ul>
    </li>
    """, unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------------------------

st.title("Lockdown")

st.markdown("""
    <p style='font-size:20px; line-height:1.6; text-align:justify;'>
    A lockdown is a comprehensive and restrictive measure implemented by governments or authorities to control the spread of a contagious disease, typically during a public health emergency. Lockdowns involve the temporary closure or severe restriction of movement, activities, and services within a specific geographic area. The primary goal of a lockdown is to minimize social contact, reduce transmission of the infectious agent, and prevent the healthcare system from being overwhelmed.    </p>
    """, unsafe_allow_html=True)

st.markdown("""
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Scope and Duration:</strong>
        <ul>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Geographic Scope:</strong> Lockdowns can be implemented at various levels, ranging from localized restrictions in specific neighborhoods to nationwide measures.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Duration:</strong> Lockdowns are typically implemented for a defined period, often subject to reassessment based on the evolving situation and public health considerations.</li>
        </ul>
    </li>

    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Restrictions and Measures:</strong>
        <ul>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Movement Restrictions:</strong> People are often required to stay at home, with limited exceptions for essential activities such as obtaining food, seeking medical care, or going to work in critical sectors.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Closure of Non-Essential Businesses:</strong> Non-essential businesses, including retail stores, entertainment venues, and educational institutions, may be temporarily closed.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Work from Home:</strong> Many organizations implement work-from-home arrangements to maintain essential functions while minimizing physical presence.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Travel Restrictions:</strong> Strict limitations on domestic and international travel may be imposed to prevent the movement of people between regions or countries.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Social Distancing:</strong> Measures to enforce social distancing, including limitations on the size of gatherings and the spacing of individuals in public spaces.</li>
        </ul>
    </li>

    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Essential Services:</strong>
        <ul>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Certain essential services:</strong> Such as healthcare, emergency services, food supply chains, and critical infrastructure, are allowed to continue operations during a lockdown.</li>
        </ul>
    </li>

    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Enforcement and Penalties:</strong>
        <ul>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Authorities often enforce:</strong> Lockdown measures through law enforcement agencies, and penalties may be imposed for violations to deter non-compliance.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Penalties can range from fines:</strong> To legal consequences, depending on the severity of the violation.</li>
        </ul>
    </li>

    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Communication and Public Awareness:</strong>
        <ul>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Clear communication from authorities:</strong> Is crucial to inform the public about the reasons for the lockdown, the expected duration, and guidelines for compliance.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Public awareness campaigns may also be conducted:</strong> To educate people about preventive measures and the importance of adhering to lockdown restrictions.</li>
        </ul>
    </li>

    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Economic and Social Impact:</strong>
        <ul>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'>Lockdowns can have significant economic and social implications, leading to disruptions in employment, income, and overall economic activity.Governments may implement economic relief measures to support individuals and businesses affected by the lockdown.</li>
        </ul>
    </li>    
    """, unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------------------------

st.title("Economic Crises")

st.markdown("""
    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Economic Crises Due to COVID-19:</strong>
        <ul>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Global Impact:</strong> The COVID-19 pandemic triggered widespread economic crises across the world.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Unemployment Surge:</strong> Lockdowns and restrictions led to a surge in unemployment as businesses, especially in sectors like hospitality and tourism, faced closures.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Business Closures:</strong> Many businesses, particularly small and medium enterprises, faced closures due to reduced demand, supply chain disruptions, and financial strain.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Supply Chain Disruptions:</strong> Global supply chains were disrupted, impacting industries reliant on international trade.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Government Spending:</strong> Governments globally increased spending on healthcare and economic relief measures, leading to fiscal challenges and increased public debt.</li>
        </ul>
    </li>

    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Impact on Financial Markets:</strong>
        <ul>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Stock Market Volatility:</strong> Financial markets experienced significant volatility, with stock markets witnessing sharp declines followed by periods of recovery.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Currency Fluctuations:</strong> Currency values fluctuated as a result of uncertainties surrounding the economic impact of the pandemic.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Interest Rate Policies:</strong> Central banks implemented various monetary policies, including interest rate cuts, to stabilize economies and encourage borrowing.</li>
        </ul>
    </li>

    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Global Economic Recession:</strong>
        <ul>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Contractions in GDP:</strong> Many countries experienced contractions in Gross Domestic Product (GDP) as economic activities declined.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Trade Disruptions:</strong> International trade suffered due to travel restrictions, supply chain interruptions, and reduced consumer demand.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Government Stimulus:</strong> Governments implemented stimulus packages to counter recessionary pressures, but sustained recovery remained a challenge.</li>
        </ul>
    </li>

    <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Unequal Impact:</strong>
        <ul>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Disproportionate Effects:</strong> The economic impact of COVID-19 was not uniform, with vulnerable populations, informal workers, and certain industries facing more significant challenges.</li>
            <li style='font-size:20px; line-height:1.6; text-align:justify;'><strong style="font-weight: bold;">Long-Term Effects:</strong> Some economists projected long-term consequences, including potential scarring effects on labor markets and persistent economic inequalities.</li>
        </ul>
    </li>
    """, unsafe_allow_html=True)
