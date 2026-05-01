
--- Page 1 ---
IEEE Access

atic Ral Rave | Opn Ao

Received 5 June 2025, accepted 21 July 2025, date of publication 29 July 2025, date of current version 4 August 2025.

Digital Object Ldentfier 10, 109/ACCESS,2025.3593523

ZEW) RESEARCH ARTICLE

Optimization and Management of Data Center
Networks: A Scoping Review on Key Themes,
Challenges, and Artificial Intelligence and
Machine Learning Approaches

KOGUL SRIKANDABALA®", (Graduate Student Member, IEEE),
KIRISHNNI PRABAGAR®", (Graduate Student Member, IEEE),

SHALINKA JAYATILLEKE®', PEARLIE ZHANG™2, RICHARD ELLERBROCK2,
SEAN RINAS2, DASWIN DE SILVA", (Senior Member, IEEE),

AND DAMMINDA ALAHAKOON!, (Member, IEEE)

Centre for Data Analytics and Cognition, La Trobe University, Melbourne, VIC 3086, Australia
?NEXTDC Ltd., Macquarie Park, NSW 2113, Australia

Corresponding author: Kogul Srikandabala (s.kogul @ Itu.edu.au)

ABSTRACT Data Center Networks (DCNs) play a critical role in enabling scalable, efficient, and
reliable digital infrastructure. This scoping review presents recent advancements in optimization and
management strategies for DCNs, with a particular focus on the application of Artificial Intelligence
(AD) and Machine Learning (ML) techniques. This study follows a structured methodology aligned with
the PRISMA-ScR protocol and extends it using Large Language Models (LLMs) to support thematic
classification and relevance screening. The analysis identified seven principal research domains: optical
networking, congestion control, flow scheduling, load balancing, Software-Defined Networking (SDN),
fault tolerance, and energy-efficient resource management. Within these domains, this study contrasts
traditional approaches with emerging Al-driven methods, highlighting their potential and limitations.
Notably, the findings revealed a lack of integrated end-to-end AI/ML frameworks capable of addressing
the multifaceted demands of modern DCN environments. Additionally, this review highlights the need for
scalable, explainable, and context-aware solutions that align with evolving DCN requirements. By analyzing
the current body of knowledge and highlighting critical research gaps, this study provides a comprehensive
foundation for future investigations into intelligent DCN design and operation.

INDEX TERMS Artificial intelligence, data center networks, machine learning, network management,
optimization, software-defined networking.

1. INTRODUCTION

In the digital age, there is a surge in the demand for network
traffic through streaming services that provide on-demand
access to entertainment, e-commerce platforms that enable
millions of real-time transactions, and social media networks
that link billions of people globally with minimal delays

The associate editor coordinating the review of this manuscript and
approving it for publication was R. K. Tripathy

in communication. The smooth operation of these services
depends on a complex network of interconnected computers
and hardware maintained in a large-scale infrastructure.
These facilities provide data availability, rapid processing,
and effective communication, thereby forming the backbone
of the Internet. Maintaining the speed, reliability, and
scalability of these infrastructures is becoming increasingly
important as society becomes more dependent on digital
technology. From guaranteeing continuous connectivity to

© 2025 The Authors, This work is licensed under a Creative Commons Attribution 4.0 License.

VOLUME 13, 2025

For more information, see https://creativecommons.org/licenses/by/4.0/

134699


--- Page 2 ---
IEEE Access’

kK. Srikandabala et al: Optimization and Management of DCNs: A Scoping Review

FIGURE 1. Number of articles published on DCs and DCNs published
during the period of 1990-2024. Research in both these areas appeared to
have gradually increased over the years but the research within DCNs has
not evolved at the same pace, thus highlighting a significant gap in this
field of research.

allowing fast data processing for AI, these services are critical
for modern technological advancements. These facilities,
known as Data Centers (DCs), form the foundation of modern
computing and communication. DCs accommodate several
computing resources that collect, store, share, manage,
and distribute large volumes of data. They consist of all
the necessary DC facility elements (space, power, and
cooling) and IT infrastructure elements (servers, storage, and
networks), based on business requirements [1].

DCs comprise various interconnected components, among
which the DCN functions as a central brain. DCNs are
specifically engineered networks that interconnect many
components within a DC and play a crucial role in day-
to-day operations [2]. Servers and storage systems within
a DC can realize their full potential only if they can
exchange data at extremely high speeds, maintain low
latency, and experience minimal downtime. Consequently,
the underlying network is vital for meeting the operational
requirements of cloud platforms, streaming services, and
enterprise applications. However, when contrasting DCNs
with conventional computer networks, such as Local Area
Networks (LAN), DCNs present a distinctive set of chal-
lenges that must be addressed. Xia et al. highlighted key
challenges in DCNs, including their massive scale, diverse
range of applications, high energy consumption, and the need
to maintain rigorous Service Level Agreements (SLAs) [2].
Previous studies have attempted to address these challenges,
as illustrated by the increasing research trends in Figure 1.
However, in the past decade, technological progress in server
hardware has been driven by Moore’s law [3], leading to
exponential increases in processing power, memory capacity,
and energy efficiency. Although computational capabilities
have advanced rapidly, DCNs have not evolved at the same
pace. Figure | illustrates the research gap observed over
the years. The increasing density and speed of servers
have placed greater demands on network infrastructure;
however, traditional networking architectures often struggle
to keep up, leading to bottlenecks, latency issues, and
inefficient data transmission. These challenges highlight the

134700

growing complexity of DCNs and emphasize the need for
continuous research and innovation to address these issues.
Although advancements in server hardware have been rapid,
DCN architectures and management strategies have not kept
pace, leading to significant bottlenecks. Understanding how
research has evolved to address these gaps is critical for
identifying key areas for further exploration.

A. RELATED SURVEYS AND REVIEWS

A considerable body of research has surveyed and reviewed
various aspects of DCNs. These reviews cover a broad range
of topics, including congestion-control solutions, traffic
management mechanisms, and optimization strategies. With
the increasing complexity and scale of modern DCNs,
researchers have sought to understand and enhance network
performance using innovative methodologies and frame-
works. Many surveys have also highlighted the emergence of
Al and ML as promising tools for automating and optimizing
DCN operations, bringing new dimensions to traditional
network management approaches.

Recent surveys on DCNs have explored various critical
themes, each addressing specific challenges and advance-
ments in the field. These themes can be categorized as
follows:

+ Optimization Strategies in DCNs: Network optimiza-
tion remains a focal point of many studies, with
researchers exploring methods such as load balancing,
traffic engineering, and routing mechanisms.
Congestion Control & Traffic Management: The
exponential growth in data traffic within DCNs has
made congestion control and traffic management essen-
tial topics of study. Several surveys have provided
comprehensive discussions on congestion control algo-
rithms, network flow management techniques, and
their practical implementation. These surveys compared
traditional methods with emerging Al-driven solutions,
emphasizing their impact on improving data throughput
and reducing packet loss.

Data Aggregation & Processing: The demand for
real-time data analytics in large-scale DCs has led to a
growing interest in data aggregation techniques. Some
surveys have investigated in-network processing and
data aggregation methodologies that enhance scalability
and computational efficiency. These studies focused
on distributed computing frameworks and their abil-
ity to streamline data flows within high-performance
networks.

Converged & High-Performance Networks: Advance-
ments in hardware and software technologies have
resulted in the development of converged network
infrastructures that integrate multiple networking
paradigms. Surveys on high-performance networking
discuss innovations, such as fiber-optic interconnects,
software-defined networking (SDN), and network
function virtualization (NFV). These studies examined

VOLUME 13, 2025


--- Page 3 ---
K. Srikandabala et al.: Optimization and Management of DCNs: A Scoping Review

IEEE Access:

TABLE 1. Survey and Review Papers on DCNs (2010-2024): This table categorizes survey papers on DCNs from 2010 to 2024 across five themes: (1)

Converged and High-Performance Networks, (2) Optimi

ion Strategies, (3) Congestion Control and Traffic Management, (4) Data Aggregation and

Processing, and (5) Next-Generation Network Technologies. Numbers indicate relevant surveys, while empty cells indicate gaps in the literature,

highlighting research trends over time.
Year Conver ged Tand High Optimization Congestion Contr ol | Data Aggregation Next Generation.
Networks Strategies in DCN Management and Processing | Network Technologies
1
2010 (4-161 : - idl =
2017 = = = = =
2012 1891 = TO} T12] =
2013 113.14] = (I5] (16.171 T8121)
2014 [22,23] = [24,25] [26]-[29] [30]-(32]
2015 B3l Bal : [35/140] es)
2016 [42] = 143] [4-146] 4748]
2017 = = [49] (50)-152] 3-155]
2018 156]-[60] (61)-[63] : [64] [65,66]
2019 [67/169] = [70] T7174] [75}-178]
2020 179] = [80] [81.82] 183]
2021 [84,85] 186] 187.88] [89,90] (91-1951
2022, 196] 197] = 198,99] :
2023 [Hoo}-[102] = [103,104] [103] =
2024 [106] T107] = = =
Total 27 T 12 33 25

the benefits and challenges of transitioning to fully
converged network architectures and their implications
for large-scale DCs.

« Next Generation Network Technologies: The rapid
evolution of DCNs has driven research into emerging
technologies that enhance scalability, efficiency, and
security. Surveys in this domain explore wireless DCNs,
such as 60 GHz networks, for high-speed, low-latency
communication, and energy-efficient networking strate-
gies to optimize power consumption. Other studies have
focused on software-defined networking (SDN) and
hyperscale architectures that leverage optical switching
and automation to improve agility and performance.
These advancements address the key challenges in
cloud and edge computing, ensuring that DCNs remain
adaptable and future-ready in the face of growing data
demands.

A more detailed breakdown of the survey papers covering
these themes from 2010 to 2024 is provided in Table 1.
This table categorizes past research efforts and highlights
key trends in DCN-related studies. As shown in Table 1,
while certain areas, such as Data Aggregation and Processing,
have received substantial attention, other aspects, including
Optimization Strategies in DCNs, remain comparatively
underexplored.

Existing surveys have provided valuable insights into
various aspects of DCN optimization, including congestion
control, traffic management, and next-generation network
technologies. However, these studies often focused on the iso-
lated aspects of DCNs rather than offering a comprehensive
synthesis. Furthermore, despite the increasing role of AI/ML
in network optimization, few studies have systematically
examined their application in DCN management. This creates

VOLUME 13, 2025

an opportunity to conduct a more structured and holistic
review that addresses gaps in the literature.

Several surveys and reviews have examined various aspects
of DCNs. Some studies have explored the potential of AI
and ML in networking, particularly for automating and
optimizing DCNs. However, we have identified the following
gaps within these surveys and reviews,

« Narrowed focus on specific aspects of the DCN -
Most studies only cover one aspect of DCNs, such as
network topology design, congestion control, or energy
efficiency. These studies provide significant insights but
do not capture the full scope of DCN research. Thus,
a scoping review capturing research in all areas of DCN
would be helpful.

Lack of systematic and scoping review approaches -
Among the few reviews that discuss all the applications
within DCNs, the majority adopt narrative review
methodologies rather than a systematic or scoping
review framework. Consequently, their coverage is often
narrow, focusing on specific techniques or isolated case
studies rather than providing a structured synthesis of the
entire research landscape. A systematic scoping review
is needed to map, categorize, and analyze the existing
body of literature, ensuring that the breadth of research
is adequately captured and that gaps in DCN studies are
clearly identified.

Limited analysis of Aland ML in DCN optimization and
management ~ Although research on DCN architectures
and optimization is extensive, most reviews over-
look AI/ML applications in network efficiency, traffic
management, and automation. As Al-driven solutions
become integral to network operations, this gap limits
our understanding of how intelligent automation and

134701


--- Page 4 ---
IEEE Access’

kK. Srikandabala et al: Optimization and Management of DCNs: A Scoping Review

predictive analytics can enhance performance, reduce
energy consumption, and improve reliability.

B. CONTRIBUTIONS

To bridge the gaps identified in Section I-A, this study
presents a scoping review of DCN research, providing a
structured analysis of key themes, methodologies, and emerg-
ing trends. By incorporating AI/ML-focused discussions and
employing a systematic scoping approach, this review aims
to offer a comprehensive understanding of how DCNs can be
optimized and managed efficiently.

The main contributions of this study are as follows.

1) A scoping review conducted following the PRISMA-
ScR guidelines [108], ensuring a systematic and
transparent approach to reviewing DCN research.

2) A novel LLM-based approach for screening and
analyzing studies, enabling efficient topic modeling
and literature review in large-scale research where
manual examination is impractical.

Identification and categorization of key research
themes in DCNs, providing insights into the primary
focus areas and trends within the field

A detailed analysis of major challenges in DCN
research and an evaluation of proposed solutions,
offering a structured overview of how researchers are
addressing critical issues.

5) An exploration of fundamental network concepts
utilized in DCN research, highlighting their role in
shaping network optimization and solution develop-
ment.

An investigation of AI/ML techniques in DCN solu-
tions, including an assessment of implementation chal-
lenges and a comparative evaluation against traditional
approaches.

By mapping the landscape of DCN research and identifying
critical gaps, this study lays the foundation for future
research on AJ-driven network optimization. The remainder
of this paper is organized as follows: Section II presents
the background and motivation for this review, establishing
the context of DCNs and the importance of Al-driven
optimization. Section III outlines the research questions
and objectives that guided this scoping review. Section IV
describes the methodology, including the literature search
strategy, selection criteria, and data extraction process.
Section V provides an overview of the foundational concepts
of DCNs, including network architectures, protocols, and
key performance metrics. Section VI reviews related survey
papers and highlights their limitations, thereby position-
ing the unique contributions of this study. Section VII
introduces a novel taxonomy for categorizing research on
Al-driven DCN optimization, organizing studies by focus
area, and methodological approach. Section VIII discusses
the main thematic areas identified in the literature. Finally,
Sections IX-XI present a comprehensive discussion, synthe-
sizing the main insights, outlining the current challenges, and
proposing future research directions.

2

4

6)

134702

Il. METHODS

This section outlines the methodology employed in this
review. This study followed the PRISMA-ScR framework,
incorporating both manual and automated techniques to
ensure systematic and unbiased selection of studies. The
review process included the formulation of research ques-
tions, identification and screening of relevant literature,
application of inclusion and exclusion criteria, and data
extraction for analysis. Given the large volume of retrieved
studies, automation techniques, including Large Language
Models (LLMs), were leveraged to enhance efficiency,
particularly in thematic screening. The following subsections
provide a detailed breakdown of this methodology.

A. RESEARCH DESIGN
This scoping review is designed to answer the following
research questions:

« RQI - What are the key research themes in DCN
and how do they contribute to the optimization and
management of DCN?

« RQ2 - What are the main challenges within each of
these themes and what solutions/breakthroughs have
been proposed to address them?

« RQ3- What fundamental network concepts support the
implementation of these solutions, and how do they
enable DCN optimization and management?

« RQ4 - How do AI/ML techniques leverage network
concepts to address DCN challenges, and how do they
compare to traditional approaches?

« RQS5 - What are the main challenges in designing,
developing and deploying AI/ML-based solutions for
the optimization and management of DCN?

The answers to these questions are discussed in detail in the
following section.

B. IDENTIFICATION AND SCREENING OF RELEVANT
STUDIES
The identification and screening processes followed the
PRISMA-ScR process, and the methodology is illustrated
in Figure 2. This approach is widely used in medicine and
biology. The review methodology was adapted for application
in the context of this study. This methodology has three
unique phases that occur serially, as illustrated in the diagram.
A comprehensive search was conducted across multiple
academic databases using the keywords “Data Center Net-
work” and “Data Centre Network” to ensure the inclusivity
of both American and British English terminology. The
search retrieved a large number of studies that were processed
for duplicate removal to eliminate redundancy. In addition,
inaccessible articles were excluded to ensure that only
retrievable and relevant studies were retained for further
screening. This step was crucial for establishing a robust
dataset while maintaining consistency in the study selection.
Given the large number of retrieved studies, manual
screening of all records was not feasible. While certain

VOLUME 13, 2025


--- Page 5 ---
IEEE Access:

K. Srikandabala et al.: Optimization and Management of DCNs: A Scoping Review

‘Studies removed before screening
Duplicate records removed (n= 192)
Records marked as ineligible by automation
tools (n = 0)

Records removed for other reasons (n = 0)

Studies Identified
from Search

(n= 1864)

v

Studios Screened Studies Excluded
Not related Tutorial (n = 12) le

‘Studies not in English (n = 0)

For each study identified from Search:
>| Prompt to check if study if a tutorial:

(n= 1672) If study is a non related tutorial: Remove else: Keep

Y
Studies Sought for
Retrieval
(n= 1660)

Studies not Retrieved
(n=0)

¥
Studies Assessed for
Eligibility
(n = 1660)

For each study:
| Prompt to check if primary focus is DCN applications:
Iyes: Keep else: Remove

Studies Excluded

(n=24) I

—— Pe

‘Studies included in
review

(n= 1636)

FIGURE 2. The PRISMA-ScR methodology followed during the study. The methodology was further extended using LLMs because the number of studies
screened was too large for manual filtering. The methodology consisted of three stages: 1) Identification: The initial search returned 1,864 records,

of which 192 were removed for duplication and other specified reasons before progressing to the screening stage. 2) Screening: A total of 1,672 studies
were screened, with 12 unrelated tutorials excluded while ensuring that all were in English. After this step, 1,660 studies were retrieved, and all were

successfully accessed. 3) El
review. LLMs were used in both screening and el
applications.

objective criteria, such as access and publication types, can be
reliably assessed using metadata, other aspects, particularly
thematic relevance, require deeper evaluation. To ensure effi-
ciency without compromising accuracy, a hybrid approach
combining automation through Large Language Models
(LLMs) and manual validation was adopted.

The large number of studies in the screening phase made
manual analysis unfeasible, necessitating automation for the
efficient identification of relevant studies. Our goal was to
eliminate bias while achieving human-level accuracy. Large
Language Models (LLMs) have been widely used in literature
reviews across disciplines. Dennstadt highlighted their role
in automating title and abstract selection in biological
research [109]. Mostafapour demonstrated how LLMs, such
as ChatGPT, assist researchers by generating early drafts,
outlines, and streamlining the review process, especially for
those with limited resources [110]. Hasan explored LLM
integration into systematic reviews, particularly for risk
of bias assessment, to enhance review rigor [111]. Chelli
further emphasized LLMs’ ability of LLMs to improve
literature searches and consolidate findings, making them

VOLUME 13, 2025

ibility and Inclusion: After assessing 1,660 studies for eligi
ibility stages to automate filtering, reducing manual workload whil

24 were excluded, lea

1,636 studies included in the final
‘ensuring relevance to DCN

invaluable for automated screening [112]. These studies
confirm that LLMs are crucial for automating and improving
the literature review process. Given the scale of studies in
this scoping review, we will leverage LLMs for thematic
identification, reducing manual workload while maintaining
accuracy.

Table 2 outlines the selection criteria used in this scoping
review. The studies were evaluated on the basis of the
following five key criteria: main theme, language, access
type, publication type, and study type. The applicability of
automation varies across different screening criteria.

« Access Type and Publication Type: These criteria can be
reliably assessed using databases like CrossRef, which
provides metadata that can be used to assess whether a
study is open-access and peer-reviewed. This step can be
fully automated using a Python script.

« Language and Study Type: While word-matching tech-
niques can identify English-language studies and distin-
guish between surveys, reviews, and original research,
some manual inspection is still required due to potential
inconsistencies in metadata and classification.

134703


--- Page 6 ---
IEEE Access’

kK. Srikandabala et al: Optimization and Management of DCNs: A Scoping Review

« Main Theme: Identifying whether a study explicitly
focuses on DCNSis the most challenging step. Keyword-
based filtering alone is insufficient because many studies
mention DCs but do not focus on DCNs. This step
requires a manual review, However, given the scale of
the dataset (thousands of studies), a Large Language
Model (LLM)-based approach is necessary to automate
thematic analysis while reducing human effort.

By integrating the CrossRef API for metadata-based filtering,
word matching for language and study type classification,
and LLMs for thematic identification, the screening process
balances efficiency and accuracy. These automated methods
significantly reduce the manual workload while maintaining
high screening precision. With the final dataset curated, the
next step involved extracting key insights from the selected
studies.

Seven key themes were extracted from the filtered papers,

which collectively represented the different focus areas
investigated by research published in the domain of DCNs.

|. MAJOR RESEARCH THEMES

The major themes identified in the literature are as follows:
+ Optical Networking and High-Speed Transmission

(N=328, 20%): With the exponential growth of data
traffic demand, Optical Networking has become the
solution offering ultra-fast transmission rates, reduced
latency, and lower power consumption.

« Congestion Control and Latency Optimization
(N=233, 14%): With high-speed transmission, the
challenge of managing network congestion and reducing
latency arises. Congestion control mechanisms are
essential for preventing packet loss, minimizing delays,
and optimizing traffic flow across the entire network.

+ Flow Scheduling and Deadline-Aware Networking
(N=216, 13%): Not all network traffic is equal,
some applications require low latency and guaranteed
deadlines. Flow scheduling is used to ensure the efficient
allocation of network resources by prioritizing critical
workloads and application-specific deadlines.

« Load Balancing and Traffic Distribution (N=123,
8%): Effective flow scheduling creates the need for load
balancing to optimize resource utilization in order to
evenly distribute network traffic,yu thereby preventing
resource over-utilization and under-utilization.
Software-Defined Networking (SDN) and Traffic
Control (N=198, 12%): The evolution of load bal-
ancing techniques necessitates programmable, flexible
traffic control mechanisms. SDN enables centralized
network management, dynamic traffic engineering, and
real-time policy adjustments.

« Fault Tolerance and Network Resilience (N=250,
15%): The implementation of SDN brings new chal-
lenges in ensuring network reliability. Fault-tolerance
mechanisms enhance network resilience by imple-
menting redundancy strategies, failure recovery, and
predictive maintenance techniques.

134704

« Energy-Efficient and Cloud Resource Management
(N=288, 18%): Optimizing network performance is
incomplete without addressing sustainability. Energy-
efficient strategies ensures sustainability by optimizing
power consumption in large-scale cloud environments

The following sections synthesize the filtered studies, cate-
gorized by their themes, to extract meaningful insights into
the challenges that drive the research, contributions made by
the research, emerging trends, and the effectiveness of various
solutions proposed. Figure 3 presents a quantitative analysis
of the distribution of themes across these factors.

Discussion on RQL

What are the key research themes in DCN and how do they
contribute to the optimization and management of DCN?

The main themes in DCN research are the seven ones

that are highlighted above. Together, they provide a basis
for current DCN studies and innovations. By addressing
important issues in terms of speed, efficiency, adaptability,
and reliability, these main themes can help optimize and
manage DCNs. Whereas congestion control and latency
optimization guarantee an uninterrupted flow of network
traffic free from bottlenecks, optical networking guarantees
a high-speed data transfer in DCNs. Critical workloads
are prioritized in flow scheduling and deadline-aware net-
working, thereby enhancing service quality. Load balancing
and traffic distribution optimize resource usage to prevent
system overload. While fault tolerance and network resilience
improve dependability by reducing service disruptions,
software-defined networking (SDN) and traffic management
add programmability and flexibility, allowing real-time
traffic adjustments. Finally, energy-efficient cloud resource
management guarantees sustainability by lowering operating
expenses and power consumption. Taken together, these
components determine the strategic direction in which DCNs
will evolve.

IV. DRIVING FORCES BEHIND DCN OPTIMIZATION:
CHALLENGES ACROSS KEY THEMES

Building upon the thematic overview presented in Section III,
this section delves deeper into each of the seven research
themes by systematically examining the key challenges,
underlying motivations, and unresolved issues that drive
ongoing optimization efforts in DCN research.

The evolution of DCNs is driven by challenges such as
scalability, congestion, security risks, and energy consump-
tion. These challenges act as driving factors that shape the
purpose of the DCN research. This section explores the
key driving forces behind DCN optimization and examines
its purpose, motivations, and challenges across the seven
fundamental themes extracted from the literature.

Optical Networking and high-speed transmission are
critical for ensuring seamless data flow in DCNs. Traditional
architectures struggle to keep up with rising data traffic,
creating the need for intelligent traffic engineering, energy-
efficient optical components, and resilient security mecha-
nisms. Research has focused on Al-driven traffic engineering,

VOLUME 13, 2025


--- Page 7 ---
kK. Stikandabala et al.: Optimization and Management of DCNs: A Scoping Review

IEEE Access:

TABLE 2. This table outlines the selection criteria applied in this scoping review of DCNs. Studies were evaluated based on relevance, language, access

type, publication type, study type, and publication year.

Criteria Inclusion Exclusion Reason
. Studies focused on DCNs and | Studies related to DCs, but not_] T° ensure that the review specifically addresses
Main Theme oeused on | : - the core topic, i.c., DNs, and avoids unrelated
their applications. specifically focusing on DCNs. coment
- shed in Enoli Studies published in Tanguages_| Non-English studies could not be screened by
Language _ | _ Studies published in English. other than English, the authors due to language limitations.
- : To allow easy access to the full text of the
Access Open-access studies. non-open-access studies. ‘
selected studies.
Non-peer-reviewed studies
Publication | Peer-reviewed journal articles | (e.g., white papers, preprints, | To ensure the credibility and scientific rigor of
Type and conference papers. blog posts, and industry the included studies.
reports).
Study Type | Review papers, survey papers, | Other types of papers that do | To cover a broad but relevant range of research
yp and original method papers. _| _ not fall into these categories. on DCNs.

ype of Challenge ® Adaptive & inteligent Systems @ Cost & Energy Efficiency @Emerging & Infrastructure Challenges @ Reliability, Resilience & Security Scalability & Performance Effiency

Optical Networking & High-Speed Transmission
Energy-Efficient & Cloud Resource Management

Fault Tolerance & Network Resilience

Congestion Control & Latency Optimization

Theme

Flow Scheduling & Deadline-Aware Networking

Load Balancing & Traffic Distribution

00

eon Coto 8

Seredsing & Deadine-aare Networeng

No of Studies

‘Type of Contributions made by the Studies

Type of Contribution @ Algorithmic @ Architectural @ Conceptual ® Methodological @ Technological

FIGURE 3. Dashboard presents the distribution of research themes categorized by (1) Type of challenges addressed, (2) Al vs. traditional approach in DCN

research, and (5) Type of contributions.

multilayer traffic optimization, and ML-based predictive
congestion control to enhance network performance [113],
[114]. Advancements in energy-efficient optical components
aim to reduce operational costs, whereas encryption and
fault-tolerance mechanisms strengthen network security and
resilience [115].

Congestion Control and Latency Optimization are vital
for reliable transmission in DCNs. However, static congestion
control mechanisms struggle to adapt to dynamic traffic
conditions, leading to performance bottlenecks and latency.
These challenges create the need for adaptive and proactive
transport optimization to enhance network responsiveness.

VOLUME 13, 2025

Research has focused on addressing these issues through
adaptive congestion control techniques [116] which dynam-
ically adjust the traffic flow to prevent congestion. Latency
reduction can be handled by employing predictive and
proactive transport strategies [117] and credit-based and RTT-
driven approaches [118].

Flow Scheduling and Deadline-Aware Networking are
essential for managing increasing traffic loads in DCNs.
As traffic loads continue to increase, ensuring low-latency
and deadline-aware transmissions is vital for supporting
real-time, high-priority traffic. These challenges create the
need for efficient traffic scheduling and accurate flow

134705


--- Page 8 ---
IEEE Access’

kK. Srikandabala et al: Optimization and Management of DCNs: A Scoping Review

classification to optimize network performance. To meet
these needs, research has explored priority-based scheduling,
adaptive flow classification, and dynamic resource allocation
as key solutions [119], [120], [121] for improving flow effi-
ciency and ensuring that critical tasks meet their deadlin

Load Balancing and Traffic Distribution are essential
to manage network traffic growth, preventing bottlenecks
and load imbalances creating the need for efficient routing
strategies. OpenFlow-based routing strategies have been
investigated to detect and mitigate elephant flows and
improve traffic scalability and distribution [122]. Switch-
migration techniques in SDN controllers have also been
explored to dynamically reduce congestion and enhance load-
balancing [123]. Studies on dynamic distributed multipath
load balancing have introduced strategies to ensure that net-
work operations remain uninterrupted during failures [124].
Furthermore, research has focused on creating adaptive
load-balancing mechanisms to minimize packet reordering
and optimize the QOS [125].

Software-Defined Networking (SDN) and Traffic Control
have emerged as a foundational approach to managing
the growing complexity of Data Center Networks (DCNs).
As traffic volume surges and application demands become
increasingly dynamic, traditional network architectures face
limitations in terms of scalability, programmability, and
adaptability. SDN addresses these issues by decoupling
the control and data planes, thereby enabling centralized
and programmable control over network behavior. However,
this architectural shift introduces new challenges, including
optimal controller placement, control-plane scalability, and
integration of hybrid SDN models. These issues have been
the focus of research exploring telemetry-based monitoring
frameworks, intrusion-aware datasets, and RPC-optimized
architectures to support efficient and resilient SDN deploy-
ment [126], [127], [128]. Furthermore, traffic control within
SDN must address emerging security threats. Studies have
shown the effectiveness of supervised machine learning mod-
els, such as SVM, K-Nearest Neighbors, and Decision Trees,
for accurate real-time traffic classification and DDoS attack
detection in emulated SDN environments [129], [130]. Fur-
ther advancements in Al-driven and Moving Target Defense
(MTD)-enabled architectures offer additional protection for
vulnerable control and data planes [131]. Collectively, these
innovations reinforce SDN’s role of SDN in shaping scalable,
intelligent, and secure DCNs capable of supporting high-
throughput, low-latency demands in evolving data-center
environments.

Fault Tolerance and Network Resilience are critical for
ensuring the reliability and stability of DCNs. However,
network breakdowns, undetected failures, and reliability
issues continue to pose risks to networks. The occurrence
of unpredictable failures in edge computing infrastructure
necessitates advanced failure prediction and mitigation strate-
gies to minimize service disruptions [132]. Cost and energy
efficiency concerns are addressed by optimizing network
architectures and reducing the dependence on expensive

134706

wired links, thereby enhancing fault resilience and reducing
operational costs [133]. These challenges create the need for
intelligent fault-tolerant mechanisms, self-healing networks,
and energy-efficient failure-recovery strategies.

Energy-Efficient and Cloud Resource Management is
pivotal in optimizing DC operations amidst various chal-
lenges. DCs consume vast amounts of power, leading to high
operational expenses and environmental impacts, creating
cost and energy efficiency challenges [134]. Traditional
network resource management struggles to dynamically
allocate resources to accommodate growing workloads,
causing scalability and performance challenges, as [135].
Concerns about reliability, resilience, and security create
the need for solutions to mitigate failures, cyber threats,
and disasters that could compromise service availabil-
ity [136]. These challenges require intelligent energy-aware
resource allocation, adaptive workload distribution, and
secure cloud management strategies to enhance sustainability
and performance. [137].

V. KEY CONTRIBUTIONS AND ADVANCEMENTS IN DCNS
The challenges that fueled DCN research have led to signif-
icant contributions across the seven themes in DCN. These
contributions can be divided into five categories: concep-
tual frameworks, methodological innovations, architectural
advancements, algorithmic improvements, and technological
development. This section explores these key contributions,
highlighting the pivotal solutions that have transformed
DCNs and set the foundation for future research.

A. CONCEPTUAL FRAMEWORKS

Conceptual frameworks (N=52, 3%) have introduced new
theories, paradigms, and foundational models that shape
future networking research. Collectively, these contributions
provide a strong theoretical foundation for improving the
efficiency of DCNs.

In optical networking, the identification of critical security
threats in wireless optical network: a pivotal conceptual
advancement that assists in highlighting vulnerabilities
for secure high-speed data transmission [138]. Congestion
control introduces a comprehensive conceptual study on
TCP coexistence and its effects on modern DC traffic,
provides vital insights into how network protocols interact,
and helps shape smarter traffic routing strategies [139].
Flow scheduling and deadline-aware networking have
been significantly improved by the introduction of the
coflow age (CA) metric concept, which enhances priority
scheduling for latency-sensitive applications [140]. In SDN-
control, the most significant conceptual innovation is the
development of traffic divergence theory, which enhances
our understanding of network traffic flow and enables
more efficient SDN-based control mechanisms [141]. The
theoretical understanding of how extra edge connectivity
strengthens network resilience and aids self-healing has
improved our knowledge of network durability [142].

VOLUME 13, 2025


--- Page 9 ---
K. Srikandabala et al.: Optimization and Management of DCNs: A Scoping Review

IEEE Access:

Similarly, the introduction of the cost-dominant fair-
ness concept for bandwidth allocation represents a major
breakthrough in optimizing resource distribution in cloud
infrastructures [143].

B. METHODOLOGICAL INNOVATIONS

Methodological innovations (N=82, 5%) focus on refin-
ing research methodologies, validation techniques, security
frameworks, and performance-testing strategies.

Key innovations in optical networking include wavelength
bank design methodology, which systematically improves
spectral efficiency, and DSP-based signal detection method-
ologies, which provide structured approaches for identi-
fying transmission errors [144]. Similarly, a methodology
integrating cooperative MPTCP models and reinforcement
learning techniques was introduced to manage network
traffic efficiently, prevent congestion, and adjust data flow
in real time to reduce delays [145]. In flow scheduling, new
store-and-forward scheduling methods have been created
to make better use of bandwidth and reduce processing
delays in time-sensitive applications [146]. In load bal-
ancing and traffic management, the HF?T methodology
has improved the distribution of network traffic, making
it more efficient in changing environments [147]. A sig-
nificant contribution to fault-tolerant mechanisms includes
a methodology involving two-stage queuing models that
was introduced to predict network delays, making networks
more resilient to failures [148]. Another pivotal novelty
is the introduction of new mathematical models to help
distribute resources more effectively, thereby cutting costs
while maintaining the performance of energy-efficient cloud
computing [149].

C. ARCHITECTURAL ADVANCEMENTS

Architectural advancements (N=479, 29%) focused on
network design, topology, and physical/logical infrastructure.
These contributions often involve novel routing structures and
system-level changes that alter how networks are phy
and logically structured.

Hybrid optical-wireless architectures integrated with
software-defined optical networking increase bandwidth
adaptability and transmission speeds [150]. Frameworks
such as RTT-based congestion control system & high-speed
packet scheduling system [151] minimizes congestions and
reduces latency. Architectures such as AIFO’s single FIFO
queue and multi-layer priority-aware scheduling enhance
traffic prioritization and deadline-aware transmission [119].
Frameworks like ConWeave introduces a fine-granularity
rerouting system that enhances load balancing in RDMA-
based networks [152]. SDN architectures use dedicated RPC
processors for microservices, which optimize latency and
performance in distributed computing environments [153].
Hierarchical fault-tolerant network architectures have been
created to enhance failure recovery mechanisms and improve
DCN resilience [154]. Al-based workload migration,

VOLUME 13, 2025

cost-efficient virtual network embedding, and energy-aware
scheduling architectures reduce power consumption and
optimize cloud infrastructure utilization [134].

D. ALGORITHMIC IMPROVEMENTS

Algorithmic improvements (N=749, 46%) involve the devel-
opment of intelligent algorithms and techniques to optimize
network functions. These contributions consist of advanced
computing techniques that influence network processes and
optimize decision-making.

Transfer learning algorithms have been proposed to
enhance link failure prediction and network performance in
high-speed optical systems [155]. Self-tuning PI congestion
control mechanisms dynamically adjust window sizes to
adapt to changing network conditions and minimize con-
gestion [116]. Fine-grained scheduling strategies have been
created to prioritize latency-sensitive applications, ensuring
efficient bandwidth allocation [119]. Highly efficient switch
migration algorithms optimize controller workloads, ensur-
ing balanced traffic flow in SDN-based networks [123].
Advanced SDN-based traffic control mechanisms with
DRL-based routing enable adaptive traffic control that
reduces congestion and improves packet delivery [156].
Algorithms leveraging deep reinforcement learning (DRL)
have been used to create self-healing networks, significantly
improving failure prediction and recovery [132]. Novel
resource allocation strategies (modified BFS algorithm) and
adaptive VM placement strategies have been proposed to
effectively schedule tasks in cloud computing environments
and optimize resource utilization while maintaining QoS
standards [134].

E. TECHNOLOGICAL DEVELOPMENTS

Technological innovation (N=274, 17%) involves new hard-
ware, network devices, transmission and communication
technologies, and software advancement.

The major contributions of technology in optical network-
ing are dual-frequency to improve optical communica-
tion stability. Clock phase caching, enabling sub-nanosecond
recovery in optical networks. Additionally, advanced mod-
ulation formats increase the efficiency of optical data trans-
mission [157], [158]. The Scalable Reliable Datagram (SRD)
protocol, a newly designed communication enhancement,
was created to enhance communication performance [159].
SmartFCT technology leverages deep reinforcement learning
(DRL) with SDN to enable real-time traffic manage-
ment [157]. A software-based multipath RDMA solution
with a tangible system, Maestro, was proposed to improve
the load distribution efficiency [160]. Another significant
contribution was the In-band Network Telemetry (INT),
an active system for real-time gray failure detection, making
it a directly applicable network resilience solution [161].
KeySFC integrates SDN with strict source routing, pro-
viding an optimized, scalable, energy-efficient networking
solution [162].

134707


--- Page 10 ---
IEEE Access’

kK. Srikandabala et al: Optimization and Management of DCNs: A Scoping Review

Discussion on RQ2
What are the main challenges within each of these themes?

The primary challenges in DCN research can be catego-
rized into key areas:

Scalability, congestion, latency, security, fault tolerance,
and energy efficiency challenges owing to rising data traffic
and complex architectures. High-speed optical networking,
adaptive congestion control, anomaly detection, intelligent
traffic management, energy-efficient resource management,
workload migration, and green networking solutions are
critical to addressing these issues.

What solutions/breakthroughs have been proposed to address
them?

To address these, DCN research has introduced architec-
tural improvements (hybrid networks, fault-tolerant topolo-
gies), algorithmic optimizations (deep learning for traf-
fic control, failure prediction), technological innovations
(in-band network telemetry, high-speed scheduling), and
methodological refinements (traffic modeling, congestion
strategies). These contributions enhance performance, secu-
rity, and sustainability, ensuring scalable and resilient DCNs.

VI. CORE NETWORKING PRINCIPLES IN DCN
Advancements in DCN research rely on a strong foundation
of network concepts. To enable intelligent and adaptive DCN
operations, researchers have focused on three key concepts:
Profiling, Anomaly Detection, and Representation.

A. MODELING AND REPRESENTATION

Representation in a DCN involves modeling network struc-
tures, traffic flows, and system behaviors for analysis,
simulations, and routing optimization. These models form the
basis for advanced DCN solutions.

Improving network representations leads to enhanced
performance. In [163], a mathematical model for Clos
networks was developed to optimize the DC topology. Sim-
ilarly, [152] focused on simulating Remote Direct Memory
Access (RDMA) behavior to analyze its impact on network
performance.

Network representation learning has also been explored
for various applications, including traffic optimization and
anomaly detection. For example, in [124], a leaf-spine
topology was used to efficiently structure DCN data,
making it suitable for AI-driven network analysis. Another
study [125] leveraged representation learning to optimize
routing protocols and reduce packet reordering, leading to
more efficient data transmission.

B. NETWORK BEHAVIOR PROFILING
Profiling is crucial for understanding traffic patterns, network
behaviors, and resource utilization, thereby enabling the
implementation of adaptive DCN management strategies.
Profiling techniques have been used to optimize DCN
performance. Research in [123] applied profiling techniques
to analyze network traffic and improve switch migration
strategies in Software-Defined Networking (SDN). Similarly,

134708

in [122], profiling methods were used to simulate network
behavior, allowing for better traffic distribution and effi-
ciency. Another study, [125], leveraged profiling to assess
packet reordering, which is essential for ensuring Quality of
Service (QoS) in DCNs. Al-driven profiling techniques are
gaining popularity. In [124], ML models were used to classify
network flows dynamically, improving resource allocation.

C. DETECTING ANOMALIES AND SECURITY THREATS
Anomaly detection is a critical component of DCN security
and performance management for identifying threats, mis-
configurations, and failures that affect network stability.

With the increasing complexity of modern DCs, detecting
anomalies in normal network behavior can help mitigate
security threats, misconfigurations, and failures. In [164],
an Al-based anomaly detection model was developed to
detect malicious activity in virtualized environments. Simi-
larly, in [165], deep learning models were trained on SDN
controller data to enhance security monitoring.

Anomaly detection also plays a crucial role in defending
against cyber threats, such as Distributed Denial-of-Service
(DDoS) attacks. Research in [166] focused on real-time
traffic monitoring to detect early signs of DDoS attacks
and prevent large-scale disruptions. Another study [167]
combined statistical methods with network telemetry to
detect traffic anomalies in cloud-based DCNs, thereby
improving network reliability.

D. INTERDEPENDENCE OF REPRESENTATION,
PROFILING, AND ANOMALY DETECTION

Representation forms the foundation by providing structured
models of network behavior. Profiling builds on this by
analyzing traffic patterns and resource usage and extracting
meaningful insights for optimization. Anomaly detection
relies on both representation and profiling to identify
deviations, detect threats, and enhance security. These three
concepts create a continuous feedback loop: representation
structures the data, profiling interprets it, and anomaly
detection refines both by identifying irregularities. Their
integration enables intelligent, adaptive, and automated DCN
management to improve the efficiency and security.

Discussion on RQ3
What fundamental network concepts support the implemen-
tation of these solutions, and how do they enable DCN
optimization and management?

The key concepts are Representation, Profiling, and
Anomaly Detection.

The representation structures network behaviors for traffic
optimization, routing efficiency, and Al-driven analysis.
Profiling examines traffic patterns and resource usage
and improves performance, load balancing, and adaptive
resource allocation. Anomaly Detection identifies security
threats, failures, and misconfigurations, aiding in intrusion
detection, DDoS mitigation, and real-time monitoring. These
concepts are interconnected, with representation providing

VOLUME 13, 2025


--- Page 11 ---
kK. Stikandabala et al.: Optimization and Management of DCNs: A Scoping Review

IEEE Access:

structure, profiling extracting insights, and Anomaly Detec-
tion refining, enabling intelligent, scalable, and secure DCN
operations.

VIL COMPARATIVE ANALYSIS OF TRADITIONAL AND
AI-BASED NETWORKING TECHNIQUES

DCNs have evolved significantly, shifting from rule-based
static techniques to adaptive AI-driven solutions. Although
traditional methods have provided stability and efficiency,
AI/ML-based solutions offer higher adaptability, predictive
capabilities, and automation. This section compares both
approaches and highlights their advantages, limitations, and
emerging trends.

A. CONVENTIONAL TECHNIQUES IN DCN

Traditional DCN methods (N=1371, 84%) rely on predefined
rules, heuristics, and static models to optimize network
operations. These techniques have been widely used for
various network functions, but often lack the flexibility
needed to adapt to real-time network fluctuations.

Optical networking commonly employs fixed-wavelength
assignment strategies to ensure stable transmission paths.
However, these methods fail to adjust in real time based
on link conditions, making them inefficient in adaptive
networks [168]. Similarly, congestion control mechanisms,
such as TCP Reno and TCP Cubic, react only after
congestion occurs, leading to scalability issues in large DCN
infrastructures [169].

To distribute traffic, scheduling and queue management
algorithms such as round-robin scheduling and weighted fair
queuing allocate resources fairly but lack responsiveness to
sudden traffic spikes [122], [123]. Similarly, rule-based SDN
flow management directs traffic through predefined paths,
providing control but lacking real-time adaptability [152],
[170].

In terms of fault tolerance, failover- and redundancy-based
techniques ensure network stability, but introduce additional
overhead and infrastructure costs [124], [125]. Likewise,
static power management strategies in cloud environments
optimize energy consumption under stable conditions but
struggle with dynamic workloads, leading to inefficient
resource utilization [122].

Traditional methods provide stability, low computational
costs, and ease of implementation. However, their reliance on
static representation for network structuring, rule-based pro-
filing for monitoring traffic, and signature-based Anomaly
Detection makes them less adaptable to real-time fluctuations
and large-scale automation, reducing their effectiveness in
dynamic environments.

B. Al AND ML DRIVEN APPROACHES IN DCN

AI/ML-based techniques (N=265, 16%) transformed DCN
management by enabling real-time decision making, predic-
tive analysis, and self-learning capabilities. Unlike static rule-
based approaches, Al-driven solutions dynamically adapt

VOLUME 13, 2025

to network conditions, predict congestion, and optimize
resource allocation.

In high-speed optical networking, AI models enhance
transmission reliability by optimizing signal modulation and
predicting link failures [171]. Similarly, Al-powered con-
gestion control enables proactive traffic flow management,
thereby preventing bottlenecks before they occur [172].
AI models leverage Representation to structure network data
efficiently.

AI/ML also improves real-time scheduling and load
balancing, dynamically adjusting network traffic, and priori-
tizing tasks based on real-time data and network conditions.
Deep Deterministic Policy Gradient (DDPG) and Deep
Reinforcement Learning algorithms optimize link weights
and traffic patterns, ensuring efficient load distribution [173].
Additionally, AlI-powered SDN controllers continuously
learn from traffic patterns, adjusting routing policies using
profiling insights to enhance dynamic load balancing,
congestion prediction, and intelligent network traffic man-
agement [174].

Furthermore, ML models such as Artificial Neural
Networks (ANN), Graph Neural Networks (GNN), and
Support Vector Machines (SVM) have been employed to
analyze historical traffic patterns and predict traffic surges,
enabling proactive resource allocation [175]. Additionally,
deep learning architectures such as Residual Networks
(ResNet) allow Al-driven systems to estimate network link
occupancy in real time, enhancing routing decisions and
overall efficiency [176].

Another key advantage of Al-driven networking is fault
tolerance and predictive maintenance. AI models detect
potential failures before they occur, thereby minimizing
the downtime and operational overhead [177]. AI also
optimizes energy-efficient networking using reinforcement
learning models to predict workload fluctuations and intelli-
gently adjust server utilization, leading to optimized power
consumption [176]. These techniques rely on Anomaly
Detection to continuously monitor network behavior, detect
performance degradation, and mitigate security threats.

By integrating AI/ML across multiple aspects of net-
work operations, modern DCNs are shifting from reactive
rule-based frameworks to proactive intelligent systems.

C. AI VS. TRADITIONAL METHODS IN DCN: KEY
DIFFERENCES AND EMERGING TRENDS
Traditional networking techniques in DCNs rely on rule-
based algorithms, static configurations, and reactive adjust-
ments, making them stable and computationally efficient, but
limited in adaptability and scalability. In contrast, AI/ML-
driven approaches introduce dynamic decision-making, pre-
dictive analytics, and automation, enabling networks to
anticipate congestion, optimize traffic flow, and adjust
resources in real time.

Traditional methods often require manual intervention and
predefined thresholds, whereas AI models continuously learn

134709


--- Page 12 ---
IEEE Access’

kK. Srikandabala et al: Optimization and Management of DCNs: A Scoping Review

from data, making proactive optimizations without human
input. In fault tolerance, conventional networks depend
on redundancy and failover mechanisms, increasing infras-
tructure costs, whereas Al-based predictive maintenance
identifies failures before they occur, reducing downtime.
Similarly, in terms of energy efficiency, traditional networks
rely on fixed threshold-based power management, often
leading to resource inefficiencies, whereas AI dynamically
adjusts power consumption based on real-time workload
demands.

Despite AI’s advantages, it requires high computational
power, extensive datasets, and ongoing optimization, making
traditional methods more interpretable, lighter, and simpler
to implement in resource-constrained environments. As AI
technologies advance, hybrid approaches that combine AI
adaptability with the stability of traditional methods are
expected to shape the future of autonomous self-optimizing
DCNs.

Discussion on RQ4
How do AI/ML techniques leverage network concepts to
address DCN challenges, and how do they compare to
traditional approaches?

AI/ML enhances DCNs by leveraging key network
concepts—Representation, Profiling, and = Anomaly
Detection—to enable real-time adaptation, predictive opti-
mization, and automation. Representation structures network
data for Al-driven traffic management, congestion control,
and routing optimization. Profiling helps analyze traffic
patterns, allocate resources efficiently, and predict failures.
Anomaly Detection strengthens fault tolerance and security
by identifying irregularities and mitigating threats in real
time.

Unlike static and rule-based methods, AI continuously
learns and adjusts, optimizing the performance dynamically.
Although AI improves scalability and efficiency, it requires
high computational power, making traditional methods more
efficient in constrained environments. Future DCNs will
integrate hybrid models, balancing AI’s adaptability with the
stability of traditional approaches for enhanced automation
and reliability

VIIL, CHALLENGES IN IMPLEMENTING AI/ML FOR DCN
OPTIMIZATION AND MANAGEMENT
The implementation of AI/ML solutions follows a struc-
tured life cycle comprising of three key phases: design,
development, and deployment [178]. In the design phase,
AI/ML systems are conceptualized, risks are assessed, and
data requirements are identified. The development phase
focuses on model selection, training, and optimization to
ensure scalability and efficiency. Finally, the deployment
phase involves integrating AI/ML models into real-world
environments, where performance, latency, and resource
constraints must be managed.

As discussed previously, there are several benefits to
integrating AI/ML-based solutions for the optimization and
management of DCNs; however, key challenges arise that

134710

FIGURE 4, The three phases of the AI/ML life cycle and their associated
challenges in DCN integration. The design phase struggles with data
acquisition, privacy, and security risks, thereby affecting Al feasibility. The
development phase faces real-time inference, scalability, and energy
efficiency challenges, requiring optimization techniques such as model
compression. The deployment phase must manage the resource
allocation and high energy consumption to ensure efficient real-time
processing. The iterative flow between phases reflects how deployment
insights refine design and development strategies.

need to be addressed. These challenges span the AI life cycle,
including data acquisition limitations, security and privacy
concerns, model adaptability, real-time inference constraints,
and resource allocation inefficiencies. Figure 4 illustrates the
challenges faced in each phase of the lifecycle. The following
sections categorize these challenges within the AI life cycle,
providing a structured analysis of the barriers to Al-driven
DCN optimization.

A. CHALLENGES IN THE DESIGN PHASE

The design phase of AI/ML integration in DCNs involves
conceptualizing models, assessing risks, and defining data
requirements. Key challenges include limited access to
high-quality training data, ensuring privacy and security,
and protecting models against adversarial attacks. In the
following subsection, we discuss these challenges in detail.

1) CHALLENGES IN ACQUIRING DATA FOR TRAINING Al/ML
MODELS

AI models require datasets to be trained, and high-quality
datasets are rare, especially in network-related domains
where data collection is sometimes limited by privacy
concerns, storage constraints, and access restrictions. Many
datasets are either proprietary or require many permissions
for access, which makes it challenging for researchers
to obtain diverse and representative data for training AI
models. This is evident in Figure 5 which illustrates
the number of datasets published every year. Real-world
datasets bring several challenges, including data availability,
complexity, and preprocessing requirements. Some datasets,
such as the InSDN dataset, collect specific network settings,
thereby restricting more general applicability [179]. Large-
scale datasets require significant computational resources
for training [180]. Another rising concern is privacy

VOLUME 13, 2025


--- Page 13 ---
K. Srikandabala et al.: Optimization and Management of DCNs: A Scoping Review

IEEE Access:

FIGURE 5. Number of datasets on DCN research proposed every year in
the past decade.

constraints, which further limit access to sensitive net-
work data, thereby complicating dataset sharing and model
reproducibility [181]. Although valuable for cybersecurity
research, incident detection datasets frequently suffer from
bias and incompleteness [182]. Additionally, real-world
network traffic traces require significant preprocessing to
manage noise and inconsistencies [183].

Synthetic datasets provide a substitute but have certain
natural limitations. Many depend on presumptions regarding
traffic models that may not entirely reflect actual behav-
ior [184]. Simulated datasets such as those based on statistical
distributions can misrepresent real traffic patterns [185].
Similarly, latency and congestion datasets assume ideal net-
work conditions, thereby overlooking unpredictable network
variables [186]. While synthetic data help address privacy
concerns, its effectiveness depends on how accurately it
mimics actual network behavior [187].

In summary, both synthetic and real-world datasets have
difficulties that interfere with the training of AI/ML models.
Dealing with these constraints requires better data-sharing
systems, updated simulation methods, and hybrid approaches
that combine synthetic and real data to improve model
adaptability.

2) SECURITY AND PRIVACY CONCERNS IN DEPLOYING
AI-DRIVEN MODELS ON DCNS

Al-based network optimization relies on vast amounts of
traffic and performance data, which are often collected from
multiple sources within a DCN. Ensuring compliance with
privacy regulations while maintaining the utility of data
is a significant challenge. Techniques such as differential
privacy and federated learning can help reduce exposure to
sensitive data but introduce trade-offs in model accuracy
and convergence speed [188], [189]. ML models used in
DCNs are susceptible to adversarial attacks, including data
poisoning and model evasion techniques, Attackers can
manipulate training data or inference inputs to degrade
the model performance, leading to incorrect network opti-
mization decisions. Ensuring robust adversarial training and
anomaly detection mechanisms is crucial for mitigating these
security threats [190], [191].

VOLUME 13, 2025

B. CHALLENGES IN THE DEVELOPMENT PHASE

The development phase of AI/ML in DCNs focuses on
model selection, training, and optimization for scalability
and efficiency. The major challenges include real-time infer-
ence constraints, high computational demands, and model
adaptability to dynamic network conditions. Solutions such
as model compression, edge processing, and reinforcement
learning help mitigate these issues but often come with
trade-offs in performance and resource utilization. In the
following subsections, we discuss these challenges in detail.

1) PERFORMANCE AND LATENCY CONSIDERATIONS

Many AI/ML techniques require real-time or near-real-
time inference to make network management decisions.
However, deep learning models, particularly those used
in predictive analytics, can introduce significant inference
latency. The challenge lies in deploying lightweight and
efficient AI models that are capable of making rapid
decisions without compromising accuracy. Techniques such
as knowledge distillation and quantization are being explored
to reduce inference overhead while maintaining model
performance [192], [193]. AI/ML models require continuous
data ingestion, processing, and inference, adding overhead to
existing DCN operations. Data preprocessing pipelines must
be carefully designed to avoid excessive computational costs.
Furthermore, the need for distributed AI processing across
network nodes introduces synchronization challenges, which
can affect the overall performance of Al-driven optimization
strategies [194], [195].

2) SCALABILITY AND ADAPTABILITY OF Al/ML MODELS

The deployment of AML models for the optimization
and management of DCNs raises significant concerns
regarding scalability and adaptability. Given that DCNs are
expansive network infrastructures that generate substantial
volumes of network telemetry data, the capacity of these
models to process and analyze such extensive datasets in
real-world prediction scenarios remains highly uncertain.
Furthermore, the training of these models requires consid-
erable computational resources, and in some cases, even the
inference phase imposes significant resource requirements.
This necessitates the adoption of strategies such as model
compression and edge processing techniques. However,
these approaches may compromise the overall performance
of the models, thereby presenting a critical trade-off that
must be carefully addressed [195], [196], [197]. DCNs are
dynamic environments. These complex networks experience
continuous fluctuations in their traffic patterns and workload
distributions. AI/ML models must dynamically adapt to
these changes, but retraining models in real time presents
challenges in terms of computational overhead and con-
vergence time. Reinforcement learning and online learning
approaches have been explored to address this issue; however,
achieving stable performance while continuously updating
the models remains a critical challenge. Furthermore, the

134711


--- Page 14 ---
IEEE Access’

kK. Srikandabala et al: Optimization and Management of DCNs: A Scoping Review

need for continuous data collection and preprocessing for
real-time learning adds additional overhead, complicating
deployment and resource management [194], [195], [198].

3) ENERGY EFFICIENCY CHALLENGES,

The integration of AI/ML models for DCN optimization
increases the overall power consumption, particularly during
the model training and inference phases. Energy-efficient
AI solutions must balance accuracy and computational
cost, requiring novel approaches such as lightweight neural
networks, hardware accelerators, and adaptive power man-
agement strategies. Future research on green AI techniques
aims to minimize the carbon footprint of Al-based DCN
management while maintaining optimization effectiveness
[192], [199].

C. CHALLENGES IN THE DEPLOYMENT PHASE

The deployment phase of AI/ML in DCNs involves
integrating models into real-world environments, while
managing performance, latency, and resource constraints.
Key challenges include efficient resource allocation, high
energy consumption, and fairness in workload distribution.
Techniques such as federated learning, cloud-edge hybrid
approaches, and adaptive power management aim to optimize
deployment, but balancing scalability and efficiency remains
a challenge. In the following subsections we discuss these
challenges in detail.

1) ENERGY EFFICIENCY CHALLENGES IN DEPLOYMENT

The deployment of AI/ML models in DCNs significantly
affects energy consumption because continuous inference
and resource management require substantial computational
power. Unlike the training phase, where energy usage is
concentrated in bursts, deployment demands sustained power
for real-time model execution, data processing, and network
optimization. High power consumption during inference can
strain existing infrastructure, increasing operational costs
and environmental impact. To address these challenges,
lightweight neural networks, hardware accelerators, and
adaptive power management strategies have been proposed.
Federated learning and cloud-edge hybrid approaches help
distribute workloads efficiently, reducing the burden on cen-
tralized DCs. However, optimizing AI deployment for energy
efficiency without compromising performance remains a
critical challenge that requires further advancement in
green AI techniques and intelligent power-aware scheduling
mechanisms.

2) RESOURCE ALLOCATION AND UTILIZATION CHALLENGES
AI/ML models have been leveraged to optimize resource
allocation in DCNs by predicting network congestion,
balancing workloads, and improving task scheduling. How-
ever, implementing ML-driven resource allocation strategies
requires high-granularity data, real-time inference, and
robust feedback loops to avoid performance degradation.

134712

Additionally, ML models must ensure fairness in resource
allocation, prevent bias in task distribution, and avoid
resource contention, which can lead to bottlenecks [198],
[200], [201]. Although AI/ML models aim to optimize
network performance, they introduce resource consumption
challenges. Training and deploying large-scale AI models
require significant computational resources, often leading
to underutilized hardware during non-peak training phases.
Implementing Al-driven workload consolidation strategies,
such as federated learning or cloud-edge hybrid approaches,
can mitigate inefficiencies. However, ensuring the efficient
deployment of AI models without increasing power con-
sumption or straining existing network infrastructure remains
aconcern [191], [192], [201].

Discussion on RQ5
What are the main challenges in designing, developing and
deploying AI/ML-based solutions for the optimization and
management of DCN?

The primary challenges in DCN research can be catego-
rized into three key areas:

« Design Challenges:

Data scarcity, privacy concerns, and adversarial risks.
Development Challenges:

Real-time inference constraints, high computational
demands, and model adaptability. Solutions such as
model compression and edge processing help but
introduce trade-offs.

Deployment Challenges:

Resource allocation, energy consumption, and fairness
concerns are addressed through federated learning and
cloud-edge strategies.

Despite advancements, ensuring efficient and scalable
Al-driven DCN solutions requires further exploration of
optimization, security, and sustainable deployment strategies.

IX. DISCUSSION
Research on DCNs has gradually grown over the last ten
years, illustrating a significant rise in studies on DCN
optimization and management. Nonetheless, DCNs remain
understudied compared to other fields of DC research.
This difference emphasizes the importance of paying more
attention to DCNs to ensure that they change in line with
developments in other critical DC technologies, storage
systems, and cloud computing. Despite this slower pace,
researchers have achieved significant progress in addressing
issues in network efficiency, reducing latency, enhancing load
balancing, and strengthening overall system resilience.
Covering congestion control, traffic engineering, load
balancing, SDN, and fault tolerance, this scoping review
outlines the major themes of DCN research. These topics
show several opportunities and challenges in this field, as well
as the collective effort to improve DCN structures and
operations. The study also explores how AI and ML are
changing network management to provide intelligent automa-
tion, traffic flow optimization, system failure prediction, and

VOLUME 13, 2025


--- Page 15 ---
K. Srikandabala et al.: Optimization and Management of DCNs: A Scoping Review

IEEE Access:

traffic flow optimization. In addition, security systems driven
by AI and ML are increasingly helping to find and reduce
cyber threats, thereby improving the resilience of modern
DCNs.

To answer the core research questions proposed, this
review highlights major advancements in DCN optimization.
Al-powered congestion control, SDN-based traffic strategies,
and adaptive load balancing are among the many solutions
being actively explored to improve efficiency. Furthermore,
emerging AI and ML applications in predictive maintenance
and energy-efficient resource management underscore the
importance of automation in DCNs. Hybrid architectures
that integrate optical and wireless technologies have been
developed, resulting in faster data transmission and reduced
latency. By combining these innovations, this review provides
a holistic perspective on the transformation of DCNs in
response to increasing computational and network demands.

Another crucial aspect of DCN research revolves around
modeling and representation, profiling, and anomaly detec-
tion, which serve as fundamental networking principles for
improving efficiency and security. Modeling and represen-
tation provide structured frameworks for analyzing network
traffic and optimizing routing, thereby allowing for more
adaptive and scalable architectures. Profiling techniques
enable a deeper understanding of traffic patterns, network
behaviors, and resource utilization, which in turn aids in the
dynamic allocation of workloads and improved congestion
management. Anomaly detection plays a vital role in
ensuring network resilience by identifying security threats,
performance bottlenecks, and points of failure before they
cause disruptions. Applying these techniques holistically
could help overcome many existing DCN challenges, paving
the way for a more robust, intelligent, and self-optimizing
network infrastructure.

By addressing RQI-RQS, our study demonstrates that
(1) telemetry-driven profiling (RQI) provides a reliable
baseline for normal network behavior; (2) feature-aware
forecasting models (RQ2) significantly improve short-term
prediction accuracy; (3) graph-based anomaly detection
(RQ3) effectively integrates structural and temporal data to
reduce false positives; (4) causal diagnosis via event graphs
(RQ4) offers interpretable insights into anomaly origins;
and (5) the proposed framework’s scalability and modularity
(RQS) support seamless deployment in large-scale data
center environments. Collectively, these findings confirm the
efficacy of an Al-driven, multistage approach to proactive
DCN monitoring and pave the way for future enhancements
in real-time network management.

One of the key contributions of this review is its structured
analysis of DCN research across multiple themes, providing a
well-rounded view of the current progress and areas that still
require attention. The scoping review methodology, guided
by PRISMA-ScR, ensures a thorough and methodological
examination of the existing research. Additionally, the
introduction of an LLM-based study screening and topic
modeling approach showcases how automation can enhance

VOLUME 13, 2025

literature reviews in large-scale research area
serve as s
practitioners. The discussion of AI and ML integration
within DCNs further deepens the understanding of both the
advantages and challenges of deploying Al-based solutions
at scale.

This review contributes to DCN research by providing a
structured synthesis of key themes, challenges, and emerging
trends across the field. By identifying gaps in areas such
as real-time anomaly detection, adaptive traffic control,
and energy-efficient network management, this review high-
lights actionable research directions for optimizing DCN
performance. In addition, the scoping methodology adopted
demonstrates how automation can enhance large-scale lit-
erature mapping, supporting more systematic and informed
advancements in DCN design and operation.

s. These insights

X. FUTURE TRENDS IN DCN RESEARCH

The evolution of DCNs has been shaped by growing demands
for automation, edge intelligence, sustainability, and security.
As data centers increasingly support cloud-native, Al-driven,
and latency-sensitive services, several promising avenues for
future research have emerged.

The integration of AI in Radio Access Networks (AI-
RAN) and Multi-access Edge Computing (AI-MEC) is set
to revolutionize network efficiency and responsiveness. AT-
RAN effectively utilizes machine learning algorithms to
optimize resource allocation and enhance user experience
by predicting traffic patterns and dynamically adjusting
network parameters [202]. Although AI-MEC also uses
edge-computing capabilities to process data closer to the
source, thus reducing latency and increasing operational
efficiency, its specific impact on real-time applications must
be explored through further research [203].

The concept of dark network operation centers (DNOCS),
characterized by minimal to no human intervention in data
management and operations, is becoming a significant trend
in the evolution of data centers. This transformation is
primarily driven by the increasing need for operational
efficiency and energy affordability within the context of cloud
computing and extensive digital infrastructure. The integra-
tion of advanced automation technologies plays a crucial role
in this shift, allowing for autonomous monitoring and control
of data center operations. For instance, new edge computing
platforms facilitate intelligent operational monitoring using
wireless and built-in sensors, which optimizes workload
distribution, thereby enhancing energy efficiency and oper-
ational reliability [204]. Moreover, innovative architectures
utilizing bidirectional DC-DC converters are important for
ensuring safety and stability in power supply systems within
DNOCs, especially given the growing operational demands
for power management in geo-distributed data centers
that support global cloud services [205], [206]. Another
essential element influencing this trend is ongoing research
on resource management strategies aimed at minimizing
costs and improving performance across various operational

134713


--- Page 16 ---
IEEE Access’

kK. Srikandabala et al: Optimization and Management of DCNs: A Scoping Review

environments [207]. The emergence of autonomous systems
in data centers signifies broader technological advancement,
where reduced human oversight can optimize efficiency and
decrease operational errors while enhancing scalability. This
shift towards a more sustainable and efficient technological
infrastructure is critical for managing increasing workloads
and energy demands [208], [209].

Sustainability has become a primary focus for future data
center network research, with significant efforts directed
towards reducing the carbon footprint and enhancing energy
efficiency. Strategies such as transitioning to renewable
energy sources, optimizing cooling systems, and implement-
ing circular economy practices are crucial for minimizing
environmental impacts [210], [211]. Studies have indicated
that substantive energy savings can be achieved through inno-
vative management practices, including energy conservation
strategies and Al-assisted resource allocation techniques
[212], [213], [214].

The integration of quantum computing into data center
security frameworks presents an unprecedented opportunity
to enhance data protection strategies. Quantum cryptography
can offer significantly higher levels of security than classical
methods by enabling secure communication channels that
are theoretically immune to eavesdropping [215]. As data
centers store vast amounts of sensitive information, the
application of these advanced security measures will become
increasingly critical for safeguarding against evolving cyber
threats [216].

The landscape of DCNs is rapidly evolving, driven by
advancements in AI, sustainability imperatives, enhanced
security protocols, and a focus on programmable infrastruc-
ture. As these trends unfold, research will play a critical
role in developing more efficient, resilient, and secure data
center operations to meet the demands of a data-driven future.
With a continued commitment to innovative approaches, the
data center industry can aspire to a more sustainable and
intelligent framework.

XI. CONCLUSION

In this scoping review, we mapped the existing body of
research and synthesized the prevailing themes, methods, and
challenges across the DCN domain. Our goal is to provide a
structured overview that highlights key trends and identifies
areas where further technology-specific investigations can
drive meaningful advancements. Several exciting research
directions are being explored. Future efforts should focus on
seamlessly integrating AI and ML solutions with real-time
network operations to enhance adaptability and predictive
capabilities. More comprehensive benchmarking frameworks
are required to evaluate Al-driven networking solutions
relative to traditional methods. Additionally, sustainability
remains a crucial aspect, and research into energy-efficient
DCN designs is key to reducing the environmental footprint
of large-scale DCs. Other promising areas include quantum
networking and blockchains, which can provide enhanced
security and decentralized network management. As DCNs

134714

continue to advance, interdisciplinary collaboration between
networking, ML, and cloud computing will shape next-
generation architectures. The growing adoption of edge com-
puting and 5G presents exciting opportunities for optimizing
data flow and minimizing latency in distributed environ-
ments. Ultimately, Al-driven solutions will likely become
the cornerstone of future DCN optimization, enabling
networks to operate with greater efficiency, intelligence, and
resilience.

Finally, this review presents a comprehensive review
of DCN research, shedding light on key innovations,
challenges, and future possibilities. By addressing gaps
in the existing literature and identifying opportunities for
further study, this study contributes to broader efforts
to enhance the performance, scalability, and sustainabil-
ity of DCNs. As technological advancements accelerate,
ongoing research and collaboration will be essential in
refining current methodologies and driving the next wave
of breakthroughs in DCN optimization. The future of DCNs
is promising, and with AI continuing to lead the way,
these networks will become more autonomous, adaptive,
and indispensable for supporting the ever-expanding digital
landscape.

APPENDIX

LIST OF ABBREVIATIONS
Abbreviation Full Term

AI Artificial Intelligence

API Application Programming Interface
BGP Border Gateway Protocol

CPU Central Processing Unit

DCN Data Center Network

DNS Domain Name System

FPGA Field-Programmable Gate Array
GPU Graphics Processing Unit
HTTP Hypertext Transfer Protocol
HTTPS Hypertext Transfer Protocol Secure
JoT Internet of Things

LAN Local Area Network

ML. Machine Learning

MPLS Multiprotocol Label Switching
NFV Network Function Virtualization
NIC Network Interface Card

OSPF Open Shortest Path First

PUE Power Usage Effectiveness

Qos Quality of Service

RIT Round-Trip Time

SDN Software-Defined Networking
SLA Service Level Agreement

SSD Solid State Drive

TCO Total Cost of Ownership

TCP Transmission Control Protocol
VLAN Virtual Local Area Network
VM Virtual Machine

WAN Wide Area Network

VOLUME 13, 2025


--- Page 17 ---
kK. Stikandabala et al.: Optimization and Management of DCNs: A Scoping Review

IEEE Access:

ACKNOWLEDGMENT
(Kogul Srikandabala and Kirishnni Prabagar contributed
equally to this work.)

REFERENCES

{1] C. Wo and R. Buyya, Cloud Data Centers and Cost Modeling. San Mateo,
CA, USA: Morgan Kaufmann, Mar. 2015

[2] W. Xia, P. Zhao, Y. Wen, and H. Xie, “A survey on data center networking
(DCN): Infrastructure and operations,” JEEE Commun, Surveys Tuts.,
vol. 19, no. 1, pp. 640-656, Ist Quart., 2017,

[3] R.R. Schaller, “Moore's law: Past, present and future,” IEEE Spectrum,
vol. 34, no. 6, pp. 52-59, Jun, 1997.

[4] R. McGeer, P. Mahadevan, and S. Banerjee, “On the complexity of power
minimization schemes in data center networks,” in Proc. IEEE Global
Telecommun. Conf. GLOBECOM, Dec. 2010, pp. 1-5.

[5] L. Popa, S. Ratnasamy, G. lannaccone, A. Krishnamurthy, and I. Stoica,
“A cost comparison of datacenter network architectures,” in Proc. 6th Int.
Conf., Nov. 2010, pp. 1-12.

[6] C. E, Rothenberg, “Re-architected cloud data center networks and their
impact on the future Internet,” in New Network Architectures. Cham,
Switzerland: Springer, 2010, pp. 179-187.

[7] L. Schares, D. M. Kuchta, and A. F. Benner, “Optics in future da
center networks,” in Proc. 18th IEEE Symp. High Perform. Interconnec
Aug. 2010, pp. 104-108.

[8] ¥. Shang, D. Li, and M. Xu, “A comparison study of energy
proportionality of data center network architectures,” in Proc. 32nd Int.
Conf. Distrib. Comput. Syst. Workshops, Jun. 2012, pp. 1-7.

(9] K. Wu, J. Xiao, and L. M. Ni, “Rethinking the architecture design of
data center networks,” Frontiers Comput. Sci., vol. 6, no. 5, pp. 596-603,
Sep. 2012

[10] R. P. Tahiliani, M. P. Tahiliani, and K. C. Sekaran, “TCP variants for
data center networks: A comparative study,” in Proc. Int. Symp. Cloud
Services Comput., Dec. 2012, pp. 57-62.

[11] C. Kachris and I. Tomkos, “The rise of optical interconnect
networks,” in Proc. 14th Int. Conf. Transparent Opt. Netw.
Jul. 2012, pp. +4.

[12] L. Xu, A. Singh, and Y. Zhan;
networks,” in Proc. Opt. Fiber Commun. Conf, 2012, pp. 1-3.

[13] XL. Wei, M. Chen, J.-H. Fan, G.-M. Zhang, and Z.-Y. Lu, “Architecture
of the data center network: Architecture of the data center network,” J.
Softw., vol. 24, no. 2, pp. 295-316, Dec. 2013.

[14] N. Farrington and A. Andreyev, “Facebook's data center network
architecture,” in Proc. Opt. Interconnects Conf., May 2013. pp. 49-50.

[15] J. Zhang, F. Ren, and C. Lin, “Survey on transport control in data center
networks,” IEEE Netw, vol. 27, no. 4, pp. 22-26, Jul. 2013.

[16] J. Perell6 et al., “All-optical packet/circuit switching-based data center
network for enhanced scalability, latency, and throughput,” IEEE Nerw:,
vol. 27, no. 6, pp. 14-22, Nov. 2013.

[7] C. Kachris and I. Tomkos, “Power consumption evaluation of all-optical
data center networks,” Cluster Comput, vol. 16, no. 3, pp. 611-623,
Aug. 2012.

[18] K. Bilal, S. U. Khan, and A. Y. Zomaya, “Green data center networks:
Challenges and opportunities,” in Proc. Ith Int. Conf. Frontiers Inf.
Technol., Dec. 2013, pp. 229-234.

[19] P.P.Jiang,C.Q. Yu, and Y. H. Peng, “Energy-saving in optical data center
networks,” Appl. Mech. Mater., vols. 411-414, pp. 634-637, Sep. 2013.

[20] M. F. Bari, R. Boutaba, R. Esteves, L. Z. Granville, M. Podlesny,
'M.G. Rabbani, Q. Zhang, and M. F. Zhani, “Data center network
virtualization: A survey,” IEEE Commun, Surveys Tuts., vol. 15, no. 2,
pp. 909-928, 2nd Quart., 2013.

[21] Y.Cai, Y. Yan, Z. Zhang, and Y. Yang, “Survey on converged data center
networks with DCB and FCoE: Standards and protocols.” [EEE Netw:,
vol. 27, no. 4, pp. 27-32, Jul. 2013

[22] A. Hendel, “Large- scale data center networks,” in Proc
Commun. Conf., 2014, pp. Th4J.1=Th4J.1

[23] F. Yao, J. Wu, G. Venkataramani, and S. Subramaniam, “A comparative
analysis of data center network architectures,” in Proc. IEEE Int. Conf.
Commun. (ICC), Jun. 2014, pp. 3106-3111

[24] Y. Ren, Y. Zhao, P. Liu, K. Dou, and J. Li, “A survey on TCP incast in data
center networks,” Int. J. Commun, Syst., vol. 27, no. 8, pp. 1160-1172,
Jul. 2012.

“Optically interconnected data center

Opt. Fiber

VOLUME 13, 2025

i271

[28]

229)

[30]

GB)

(32]

(331

(34)

BT]

[40]

au

[42]

[43]

(44)

H. X. Wu, X. L. Yang, and M. Zhang,
center networks: A survey and new perspectives.”
vols. 462-463, pp. 1028-1035, Nov. 2013.

Ki. Kitayama, Y.-C. Huang, Y. Yoshida, R. Takahashi, and
M. Hayashitani, “Optical packet and path switching intra-data center
network: Enabling technologies and network performance with intelligent
flow control,” in Proc. Eur. Conf. Opt. Commun. (ECOC), Sep. 2014,
pp. 1-3.

M. Fayyaz and K. Aziz, “Classification of optical interconnects in
data center networks,” in Proc. 12th Int. Conf. Frontiers Inf. Technol.,
Dec. 2014, pp. 61-66.

N. Calabretta, W. Miao, S. D. Lucente, J. Luo, and H. J. $. Dorren,
“Scalable and low latency optical packet switching architectures for high
performance data center networks,” in Adv Photon, Commun., 2014

K. Kitayama, Y. Huang, Y. Yoshida, R. Takahashi, and M. Hayashitani,
“OPS/OCS intra-data center network with intelligent flow control,” in
Adv. Photon. Commun., 2014.

H. Qi, M. Shiraz, J.-Y. Liu, A. Gani, Z. A. Rahman, and T. A. Altameem,
“Data center network architecture in cloud computing: Review, taxon-
‘omy, and open research issues,” J. Zhejiang Univ: Sci. C, vol. 15, no. 9,
pp. 776-793, Sep. 2014.

A. Hammadi and L. Mhamdi, “A survey on architectures and energy
efficiency in data center networks,” Comput. Commun.,.vol. 40, pp. 1-21,
Mar. 2014.

K. Bilal, S. U. R. Malik, O. Khalid, A. Hameed, E. Alvarez,
V. Wijaysekara, R. Irfan, S. Shrestha, D. Dwivedy, M. Ali, U. S. Khan,
A. Abbas, N. Jalil, and S. U. Khan, “A taxonomy and survey on green
data center networks.” Future Gener. Comput. Syst., Vol. 36, pp. 189-208,
Jul, 2014.

B. Maggs, “A universal approach to data center network design,” in Proc
26th ACM Symp. Parallelism Algorithms Archit., Jun, 2014, p. 246.

A. Lonare and V. Gulhane, “Addressing agil
balance in fat-tree data center network—A review,” in Proc. 2nd Int. Conf.
Electron. Commun. Syst. (ICECS), Feb. 2015, pp. 965-971.

M. Fayyaz, K. Aziz, and G. Mujtaba, “Blocking probability in optical
interconnects in data center networks,” Photonic Netw. Commun. vol. 30,
no. 2, pp. 204-222, May 2015.

W. Hou, L. Guo, Y. Liu, C. Yu, and Y. Zong, “Resource manage-
ment and control in converged optical data center networks: Survey
and enabling technologies,” Comput. Netw., vol. 88, pp. 121-135,
Sep. 2015.

R. Takahashi, T. Segawa, S. Ibrahim, T. Nakahara, H. Ishikawa,
A. Hiramatsu, Y.-C. Huang, and K.-i, Kitayama, “Torus data center
network with smart flow control enabled by hybrid optoelectronic routers
[Invited].” J. Opt. Commun. Netw., vol. 7, no. 12, pp. B141-B152,
Dec. 2015.

C. Kachris and I, Tomkos, “A roadmap on optical interconnects in
data centre networks,” in Proc. 17th Int. Conf. Transparent Opt. Netw.
(ICTON). Jul. 2015, pp. 1-3

K-I. Kitayama, Y.-C. Huang, Y. Yoshida, R. Takahashi, T. Segawa,
S. Ibrahim, T. Nakahara, Y. Suzaki, M. Hayashitani, Y. Hasegawa,
Y. Mizukoshi, and A. Hiramatsu, “Torus-topology data center network
based on optical Packev/Agile circuit switching with intelligent flow
management,” J. Lightw. Technol. vol. 33, no. 5, pp. 1063-1071,
Mar, 1, 2015.

R. Rojas-Cessa, Y. Kaymak, and Z. Dong, “Schemes for fast transmission
of flows in data center networks.” IEEE Commun. Surveys Tuts., vol. 17,
no. 3, pp. 1391-1422, 3rd Quart, 2015.

E, Baccour, S. Foufou, R. Hamila, and M, Hamdi, “A survey of wireless
data center networks,” in Proc. 49th Annu. Conf. Inf. Sci. Syst. (CISS),
Mar. 2015, pp. 1-6.

C. Yu, W. Hou, and L. Guo, “A survey on virtual network embedding
in optical cloud data center networks,” in Proc. Int. Conf. Sofiw. Netw.
(ICSN), May 2016, pp. 1-5.

P. Sreckumari and J-1. Jung, “Transport protocols for data
center networks: A survey of issues, solutions and challenges,”
Photonic Netw. Commun. vol. 31, no. 1, pp. 112-128,
Aug. 2015.

A. Shpiner and E. Zahavi, “Race cars vs. Trailer trucks: Switch buffers
sizing vs. Latency trade-offs in data center networks,” in Proc. IEEE
24th Annu. Symp. High-Performance Interconnects (HOTI), Aug. 2016,
pp. 53-59.

‘ongestion control in data
* Appl. Mech. Mater.,

vol.

and improving load

134715


--- Page 18 ---
IEEE Access’

kK. Srikandabala et al: Optimization and Management of DCNs: A Scoping Review

[45]

146]

[47]

[48]

[50]

(51)

[52]

[53]

[54]

[55]

[56]

[57]

[58]

159]

[60]

{61}

[62]

[63]

[64]

[65]

[66]

[67]

O. Raz, G. Guelbenzu, T. Li, C. Li, W. Miao, F. Yan, H. J. S. Dorren, P.
Stabile, and N. Calabretta, “Optical solutions for the challenges of mega-
ize data center networks,” in Proc. Opt. Fiber Commun. Conf. Exhib.
(OFC), Mar. 2016, pp. 1-3.

M. Fayyaz, K. Aziz, and G. Mujtaba, “Performance analysis of optical
interconnects’ architectures for data center networks: Do you have
a subtitle? If so, write it here.” Cluster Comput., vol. 19, no. 3,
pp. 1139-1161, Jul. 2016.

T.Chen, X. Gao, and G. Chen, “The features, hardware, and architectures
of data center networks: A survey.” J. Parallel Distrib. Comput., vol. 96,
pp. 45-74, Oct. 2016.

V. D. Chakravarthy and V. Nagarajan, “Techniques for optimizing power
utilization in data center network architectures: A survey report,” Indian
J. Sci. Technol., vol. 9, no. 37, pp. 1-6, Oct. 2016.

T. Hafeez, N. Ahmed, B. Ahmed, and A. W. Malik, “Detection and
mitigation of congestion in SDN enabled data center networks: A survey,”
IEEE Access, vol. 6, pp. 1730-1740, 2018

G.C. Sankaran and K. M. Sivalingam, “A survey of hybrid optical data
center network architectures,” Photonic Netw. Commun., vol. 33, n0. 2,
pp. 87-101, Jul. 2016.

S. Yan, “Recent research in intra/inter-data center network communica-
tion,” in Proc. Asia Commun, Photon. Conf. (ACP), Nov. 2017, pp. 1-12.
D. Zhang, H. Guo, G. Chen, Y. Zhu, H. Yu, J. Wang, and J. Wu,
“Analysis and experimental demonstration of an optical switching
enabled scalable data center network architecture,” Opt. Switching Netw:,
vol. 23, pp. 205-214, Jan. 2017.

Y. Tang, H. Guo, X. Li, and J. Wu, “Experimental demonstration of
efficient topology reconstruction in optical switching based data center
network.” in Proc. 16th Int. Conf. Opt. Commun. Netw. (ICOCN),
Aug. 2017, pp. 1-3.

B. Dai, G. Xu, B. Huang, P. Qin, and Y. Xu, “Enabling network innovation
in data center networks with software defined networking: A survey,
Netw. Comput. Appl., vol. 94, pp. 33-49, Sep. 2017.

S. Subramaniam, “Optics in data center networks,” Proc. Adv. Photon
2017 (IPR, NOMA, Sensors, Netw., SPPCom, PS) OSA, 2017, Paper
NeW2B.2, doi: 10.1364/networks.2017.new2b.2.

Z. Han and L. Yu, vey of the BCube data center network
topology.” in Proc. IEEE IEEE 4th Int. Conf. Big Data Secur. Cloud
(BigDataSecurity) Int. Conf. High Perform. Smart Comput., (HPSC)
IEEE Int. Conf. Intell. Data Secur. (IDS), May 2018, pp. 229-231

Z. Han and W. Zhang, “A summary of the BCCC data center network
topology.” in Proc. IEEE IEEE 4th Int. Conf. Big Data Secur. Cloud
(BigDataSecurity) Int. Conf. High Perform. Smart Comput., (HPSC)
IEEE Int. Conf. Intell. Data Secur. (IDS), May 2018, pp. 270-272.

Z. Chkirbene, R. Hamila, and S. Foufou, “A survey on data center
network topologies.” in Ubiquitous Networking (Lecture notes in
computer science). Cham, Switzerland: Springer, 2018, pp. 143-154.
A.N. Quttoum, “Interconnection structures, management and routing
challenges in cloud-service data center networks: A survey,” Int. J.
Interact. Mobile Technol. (iJIM), vol. 12, no. 1, p. 36, Jan. 2018.

X. Jiang, M. D. Feuer, and M. V. Bnyamin, “Advanced modulation
formats for large capacity data center networks,” Proc. SPIE, vol. 10536,
p. 71, May 2018.

K. Wang, Q. Zhou, S. Guo, and J. Luo, “Cluster frameworks for efficient
scheduling and resource allocation in data center networks: A survey,”
IEEE Commun. Surveys Tuts., vol. 20, no. 4, pp. 3560-3580, 2018.

S. Wang, J. Zhang, T. Huang, J. Liu, T. Pan, and Y. Liu, “A survey of
coflow scheduling schemes for data center networks,” /EEE Commun.
Mag., vol. 56, no. 6, pp. 179-185, Jun. 2018.

J. Zhang, F.R. Yu, S. Wang, T. Huang, Z. Liu, and Y. Liu, “Load balaneing
in data center networks: A survey,” IEEE Commun. Surveys Tuts., vol. 20,
no. 3, pp. 2324-2352, 3rd Quart., 2018.

S. Huang, D. Dong, and W. Bai, “Congestion control in high-speed
lossless data center networks: A survey,” Future Gener. Comput. Syst.,
vol. 89, pp. 360-374, Dec. 2018.
A. Tzanakaki, L. Wosinska, L. Schares, H. Liu, and D. Simeonidou,
“Special issue on optical data center networks,” J. Opt. Commun. Netw.,
vol. 10, no. 7, p. ODC1, Jun, 2018.

A. Pilimon, A. M. Kentis, S. Ruepp, and L. Dittman, “Analysis of traffic
engineering capabilities for SDN-based data center networks,” in Proc.
Sth Int. Conf. Softw. Defined Syst. (SDS), Apr. 2018, pp. 211-216.

R. R. Reyes, S. Sultana, V. V. Pai, and T. Bauschert, “Analysis
and evaluation of CAPEX and OPEX in intra-data centre network
architectures,” in Proc. IEEE Latin-Amer. Conf. Commun. (LATINCOM),
Nov. 2019, pp. 1-6.

134716

[68]

[69]

[70]

a

(72]

(73]

(74)

{75}

[76]

(7)

[78]

[79]

[80]

{81}

[82]

[83]

[84]

[85]

[86]

[87]

[88]

[89]

[90]

[91]

X. Du, Z. Han, and Y. Huangfu, “A summary of Hamiltonian based on
data center network.” in Proc. IEEE Sth Int. Conf. Big Data Secur: Cloud
(BigDataSecurity) Int. Conf. High Perform. Smart Comput., (HPSC)
IEEE Int. Conf. Intell. Dara Secur. (IDS), May 2019, pp. 189-191

M. Klymash, O. Shpur, O. Lavriv, and N. Peleh, “Information security
in virtualized data center network,” in Proc. 3rd Int. Conf. Adv. Inf.
Commun. Technol. (AICT), Sul. 2019, pp. 419-422.

M. Alipio, N. M. Tiglao, F. Bokhari, and S. Khalid, “TCP incast solutions
in data center networks: A classification and survey,” J. Netw: Comput.
Appl., vol. 146, Nov. 2019, Art. no, 102421

S. Ibrahim and T. Hashimoto, “Novel lambda-rich data
From underlying principles to candidate technologie:
Fiber Commun. Conf: (OFC), 2019, pp. 1=14.

L. Gonzalez-Naharro, J. Escudero-Sahuquillo, P. J. Garcia, F. J. Quiles,
J. Duato, W. Sun, X. Yu, and H. Zheng, “Modeling traffic workloads in
data-center network simulation tools,” in Proc. Int. Conf: High Perform.
Comput. Simul, (HPCS), Sul. 2019, pp. 1036-1042.

Y. Tang, H. Guo, Y. Zhu, T. Yuan, X. Gao, C. Wang, and J. Wu,
“Effectively reconfigure the optical circuit switching layer topology in
data center network by OCBridge,” J. Lightw. Technol., vol. 37, no. 3,
pp. 897-908, Feb. 1, 2019.

A. Sharma and R. G. Sangeetha, “Comparativ
interconnection architectures in data center networks,
vol. 40, no. 3, pp. 225-238, Jan. 2018.

B. Pavithra, S. Suchitra, S. Sophia, and J. L. George, “SDN based energy
efficient cloud data center networks,” Int. J. Innov. Technol. Exploring
Eng., Vol. 8, no. 12, pp. 4250-4256, Oct. 2019.

E, Baccour, S. Foulou, R. Hamila, and A. Erbad, “Green data center
networks: A holistic survey and design guidelines,” in Proc. 15th
Int. Wireless Commun. Mobile Comput. Conf. (IWCMC), Jun. 2019,
pp. 1108-1114.

A. S, Hamza, “Recent advances in the design of optical wireless data
center networks.” Proc. SPIE, vol. 10945, p. 20, Feb. 2019.

A. Celik, B. Shihada, and M. Alouini, “Optical wireless data center
networks: Potentials, limitations, and prospects,” Proc. SPIE, vol. 10945,
p. 18, Feb. 2019.

V. Sharma and R. Mishra, “A comprehensive survey on data center
network architectures,” in Proc. 8th Int. Conf. Rel, Infocom Technol.
Optim. (Trends Future Directions) (ICRITO), Jun. 2020, pp. 222-228.
Y-C. Tsai, T-C. Hou, and M.-C. Chiu, “Design of TCP congestion
control in data center networks based on stable round trip time,” in Proc.
8th Int. Conf. Commun. Broadband Netw., Apt. 2020, pp. 40-44.

Z. Guo, S. Liu, and Z.-L. Zhang, “Traftic control for RDMA-enabled data
center networks: A survey,” IEEE Syst. J., vol. 14, no. 1, pp. 677-688,
Mar, 2020.

L. Zhang, J. Chen, E. Agrell, R. Lin, and L. Wosi inabling tech-
nologies for optical data center networks: Spatial division multiplexing,”
J. Lightw. Technol., vol. 38, no. 1, pp. 18-30, Jan. 1, 2020.

S. Wang, H. Cao, and L. Yang, “A survey of service function chains
orchestration in data center networks,” in Proc. IEEE Globecom
Workshops (GC Wkshps), Dec. 2020, pp. 1-6.

G. S. Kuaban, T. Atmaca, A. Kamli, T. Czachérski, and P, Czekalski,
“Performance analysis of packet aggregation mechanisms and their
applications in access (E.G., ToT, 4G/5G), core, and data centre
networks,” Sensors, vol. 21, no. 11, p. 3898, Jun. 2021.

T. Sahoo, S. K. Naik, and K. K. Das, “Data center networks: The
evolving scenario,” in Smart Innovation, Systems and Technologies,
2021, pp. 601-610.

J. Jia and G. Liu, “Data center networks: Address scheming, traffic
distribution, and load balancing,” in Proc. IEEE Int. Conf. Comput. Sci.,
Artif. Intell. Electron, Eng. (CSAIEE), Aug. 2021, pp. 309-318,

H. Amari, W. Louati, L. Khoukhi, and L. H. Belguith, “TCP ineast solu-
nis in data center networks: Survey.” in Advances in Intelligent Systems
and Computing. Cham, Switzerland: Springer, 2021, pp. 535-545.
W.Li, J. Liu, S. Wang, T. Zhang, S. Zou, J. Hu, W. Jiang, and J. Huang,
“Survey on traffic management in data center network: From link layer
to application layer,” JEEE Access, vol. 9, pp. 38427-38456, 2021

Y. Tang, T. Yuan, B. Liu, and C. Xiao, “Effective-flow schedule for optical
circuit switching based data center networks: A comprehensive survey.”
Comput. Netw, vol. 197, Oct. 2021, Art. no. 108321

H. Dong, A. Munir, H. Tout, and Y. Ganjali, “Next-generation data
center network enabled by machine learning: Review, challenges, and
opportunities,” /EEE Access, vol. 9, pp. 136459-136475, 2021.

C. Terzi and I. Korpeoglu, “60 GHz wireless data center networks: A
survey,” Comput. Netw, vol. 185, Feb. 2021, Art. no. 107730.

nter network:
in Proc. Opt.

study of optical
J. Opt. Commun.,

VOLUME 13, 2025


--- Page 19 ---
kK. Stikandabala et al.: Optimization and Management of DCNs: A Scoping Review

IEEE Access:

[92]

[93]
[94]

[95]

[96]

[97]

[98]

[99]

[100]

01)

[102]

[103]

[104]

1105]

[106]

107)

{108}

[109]

[110]

any

(112)

13)

T. Niu and H. Li, “A survey of energy-efficient methods in data center
networks based on software defined network,” in Proc. IEEE Conf.
Telecommun., Opt. Comput. Sci. (TOCS), Dec. 2021, pp.
R. Tang, “Innovations for data center network optimization,”
Conf. Comput. Inf. Sei. Artif. Intell. (CISAI), Sep. 2021, pp. 610-615
A.M. Abdelrahman, J.J. P.C. Rodrigues, M. M. E. Mahmoud, K. Saleem,
A.K. Das, V. Korotaey, and S. A. Kozlov, “Software-defined networking
security for private data center networks and clouds: Vulnerabilities,
attacks, countermeasures, and solutions,” Int. J. Commun. Syst., vol. 34,
no. 4, Dec. 2020, Art. no, 4706.

M. Nooruzzaman and X. Fernando, “Hyperscale data center networks
with transparent HyperX architecture,” IEEE Commun. Mag., vol. 59,
no. 6, pp. 120-125, Jun, 2021

A.C. Castillo, “Various network topologies and an analysis comparative
between fat-tree and BCube for a data center network: An overview.
Proc. IEEE Cloud Summit, Oct. 2022, pp. 1-8.

D. Li, G. Cao, L. Xiao, J. Yao, and X. Cao, “Research progress and trend
of coflow time-optimal scheduling in data center network,” in Proc. Int.
Conf. Artif: Intell. Secur., 2022, pp. 560-572.

C. Xie and B. Zhang, “Scaling optical interconnects for hyperscale
data center networks,” Proc. IEEE, vol. 110, no. 11, pp. 1699-1713,
Nov. 2022

B.Li, T. Wang, P. Yang, M. Chen, and M. Hamdi, “Rethinking data center
networks: Machine learning enables network intelligence,” J. Commun,
Inf. Netw. vol. 7, no. 2, pp. 157-169, Jun, 2022.

S. Pachnicke, S. Oettinghaus, S. Calabré, T. Wettlin, N. Stojanovic, and
T. Rahman, “Digital signal processing for 1.6 Tb/s+ intra-data center
networks,” in Proc. IEEE Photon. Conf. (IPC), Nov. 2023, pp. 1-2.

W. Xue, Z. Han, and X. Du, “Review of new data center network
structure,” in Proc. 25th Int. Conf. Adv. Commun. Technol. (ICACT),
Feb. 2023, pp. 232-235.

M. Zhao, Z. Han, and X. Du, “A survey of data center network topology
structure,” in Proc. 25th Int. Conf. Adv. Commun, Technol. (ICACT),
Feb. 2023, pp. 303-309.

C. Nandhini and G. P. Gupta, “Exploration and evaluation of congestion
control algorithms for data center networks,” Social Netw, Comput. Sci.,
vol. 4, no. 5, Jun, 2023, Art. no. 509,

R. Ji, L. Ji, K. Gu, J. Wu, and G. Lei, “A survey of multipath
transport mechanism in data center networks.” in Proc. Mobile Networks
Manag., in Lecture Notes of the Institute for Computer Sciences, Social
Informatics and Telecommunications Engineering. Cham, Switzerland:
Springer, 2023, pp. 373-385.

A. Feng, D. Dong, F. Lei, J. Ma, E. Yu, and R. Wang, “In-network
aggregation for data center networks: A survey,” Comput. Commun.,
vol. 198, pp. 63-76, Jan. 2023.

S. Hu, X. Zhang, C. Li, H. Yin, X. Li, and X. Xin, “Latest advances in
VCSEL technology for next-generation data center network [Invited],”
Chin. Opt. Lett., vol. 22, no. 11, 2024, Art. no. 111401.

Y. Liu, T. Yu, Q. Meng, and Q. Liu, “Flow optimization strategies in data
center networks: A survey.” J. Netw. Comput. Appl., vol. 226, Jun. 2024,
Art. no. 103883.

A.C. Tricco et al., “PRISMA extension for scoping reviews (PRISMA-
SeR): Checklist and explanation,” Ann, Internal Med., vol. 169, no. 7,
pp. 467-473, Oct. 2018.

E Dennstidt, J. Zink, P. M. Putora, J. Hastings, and N. Cihoric, “Title and
abstract screening for literature reviews using large language models: An
exploratory study in the biomedical domain,” Systematic Rev., vol. 13,
no. 1, Jun. 2024, Art. no. 158.

™M. Mostafapour, J. H. Fortier, K, Pacheco, H. Murray, and G. Garber,
“Evaluating literature reviews conducted by humans versus ChatGPT:
Comparative study,” JMIR AI, vol. 3, Aug. 2024, Art. no. 56537.

B. Hasan, $. Saadi, N. S. Rajjoub, M. Hegazi, M. Al-Kordi, F. Fleti, M
Farah, I. B, Riaz, I. Banerjee, Z. Wang, and M. H. Murad, “Integrating
large language models in systematic reviews: A framework and case study
using ROBINS-1 for risk of bias assessment,” BMJ Evidence-Based Med.,
vol. 29, no. 6, pp. 394-398, Dec. 2024.

M. Chelli, J. Descamps, V. Lavoué, C. Trojani, M. Azar, M. Deckert, J.-L.
Raynier, G. Clowez, P. Boileau, and C. Ruetsch-Chelli, “Hallucination
rates and reference accuracy of ChatGPT and bard for systematic
reviews: Comparative analysis,” J. Med. Internet Res., Vol. 26, May 2024,
Art. no. €53164.

K. Wang, T. Song, Y. Wang, C. Fang, J. He, A. Nirmalathas, C. Lim,
E, Wong, and S. Kandeepan, “Evolution of short-range optical wireless
communications,” J. Lightw, Technol, vol. 41, no. 4, pp. 1019-1040,
Feb. 15, 2023.

VOLUME 13, 2025

(114)

U5]

[116]

U7)

(118)

(119)

[120]

(121)

[122]

{123}

[124]

[125]

1126]

127)

[128]

[129]

[130]

(131)

1132]

1133]

134]

J.Wei, T. Rahman, 8. Calabro, N. Stojanovic, L. Zhang, C. Xie, Z. Ye, and
M. Kuschnerov, “Experimental demonstration of advanced modulation
formats for data center networks on 200 Gb/s lane rate IMDD links,”
Opt. Exp., vol. 28, no. 23, p. 35240, Nov. 2020.

C. Browning, Q. Cheng, N. C. Abrams, M. Ruffini, L. ¥. Dai, L. P. Barry,
and K. Bergman, “A silicon photonic switching platform for flexible
converged centralized-radio access networking,” J. Lightw. Technol.,
vol. 38, no. 19, pp. 5386-5392, Oct. 1, 2020.

P, Taheri, D. Menikkumbura, E. Vanini, S. Fahmy, P. Eugster, and
T. Edsall, “RoCC,” in Proc. 16th Int. Conf. Emerg. Netw. Exp. Technol.,
Nov. 2020, pp. 17-30.

C. Tian, B. Li, L. Qin, J. Zheng, J. Yang, W. Wang, G. Chen, and
W. Dou, “P-PFC: Reducing tail latency with predictive PFC in lossless
data center networks,” IEEE Trans. Parallel Distrib. Syst., vol. 31, no. 6,
pp. 1447-1459, Jun, 2020.

Y. Gilad, T. Hlavacek, A. Herzberg, M. Schapira, and H. Shulman,
“Perfect is the enemy of good: Setting realistic goals for BGP security,”
in Proc. 17th ACM Workshop Hot Topics Netw., Nov. 2018, pp. 57-63,
W-X. Liu, J. Cai, Y. Wang, Q. C. Chen, and J.-Q. Zeng, ““Fine-grained
flow classification using deep learning for software defined data center
networks,” J. Netw. Comput. Appl., vol. 168, Oct. 2020, Art. no. 102766.
A. Yu, H. Yang, K. K. Nguyen, J. Zhang, and M. Cheriet, “Burst traffic
scheduling for hybrid E/O switching DCN: An error feedback spiking
neural network approach,” IEEE Trans, Netw, Service Manage., vol. 18,
no. 1, pp. 882-893, Mar. 2021

S. Luo, H. Yu, K. Li, and H. Xing, “Efficient file dissemination in data
center networks with priority-based adaptive multicast,” IEEE J. Sel.
Areas Commun., vol. 38, no. 6, pp. 1161-1175, Jun. 2020.

X. Shi, Y. Li, H. Xie, T. Yang, L. Zhang, P. Liu, H. Zhang, and Z. Liang,
“An OpenFlow-based load balancing strategy in SDN.” Comput., Mater.
Continua, vol. 62, no. 1, pp. 385-398, 2020.

Y. Liu, H. Gu, F. Yan, and N. Calabretta, “Highly-efficient switch
migration for controller load balancing in elastic optical inter-datacenter
networks,” EEE J. Sel. Areas Commun., vol. 39, no. 9, pp. 2748-2761,
Sep. 2021

F, Wang, H. Yao, Q. Zhang, J. Wang, R. Gao, D. Guo, and M. Guizani,
“Dynamic distributed multi-path aided load balancing for optical data
center networks.” IEEE Trans. Netw. Service Manage., vol. 19, no. 2,
pp. 991-1005, Jun. 2022.

J. Huang, W. Lyu, W. Li, J. Wang, and T. He, “Mitigating packet
reordering for random packet spraying in data center networks,”
IEEE/ACM Trans. Netw., vol. 29, no. 3, pp. 1183-1196, Jun, 2021

Y. Lin, Y. Zhou, Z. Liu, K. Liu, Y. Wang, M. Xu, J. Bi, Y. Liu, and
J. Wu, “NetView: Towards on-demand network-wide telemetry in the
data center,” Comput, Netw., vol. 180, Oct. 2020, Art. no, 107386.

M. S. Elsayed, N.-A. Le-Khac, and A. D. Jurcut, “InSDN: A novel SDN
ntrusion dataset.” IEEE Access, vol. 8, pp. 165263165284, 2020.

M. Sutherland, S. Gupta, B. Falsafi, V. Marathe, D. Pnevmatikatos,
and A. Daglis, “The NEBULA RPC-optimized architecture,” in Proc
ACM/IEEE 47th Annu. Int, Symp. Comput. Archit. (ISCA), May 2020,
pp. 199-212.

A. Hirsi, L. Audah, A. Salh, N. M. Sahar, S. Ahmed, and M. A. Alhartomi
“DDoS anomaly detection in software-defined networks: An evaluation
of machine learning techniques for traffic classification and prediction,”
in Proc. Int. Conf. Future Technol. Smart Soc. (ICFTSS), Aug. 2024,
pp. 100-105, doi: 10.1 109/icftss61 109.2024. 10691328.

A. Hirsi, L. Audah, A. Salh, M. A. Alhartomi, and S. Ahmed,
“Detecting DDoS threats using supervised machine learning for traffic
classification in software defined networking,” IEEE Access, vol. 12,
pp. 166675-166702, 2024, doi: 10.1 109/ACCESS.2024.3486034.

A. H. Abdi, L. Audah, A. Salh, M. A. Alhartomi, H. Rasheed,
S. Ahmed, and A. Tahir, “Security control and data planes of SDN:
A comprehensive review of traditional, AI, and MTD approaches to
security solutions.” /EEE Access, vol. 12, pp. 69941-69980, 2024, doi
10.1 109/ACCESS.2024.3393548.

A. Aral and I. Brandic, “Learning spatiotemporal failure dependencies for
resilient edge computing services.” IEEE Trans. Parallel Distrib. Syst.,
vol. 32, no. 7, pp. 1578-1590, Jul. 2021

B. Cao, J. Zhao, P. Yang, Y. Gu, K. Muhammad, J. J. P. C. Rodrigues,
and V. H.C. de Albuquerque, “Multiobjective 3-D topology optimization
of next-generation wireless data center network,” JEEE Trans. Ind.
Informat., vol. 16, no. 5, pp. 3597-3605, May 2020.

K. Devi R., M. Gurusamy, and V. P., “An efficient cloud data center
allocation to the source of requests,” J. Organizational End User
Comput., vol. 32, no. 3, pp. 23-36, Jul. 2020.

134717


--- Page 20 ---
IEEE Access’

kK. Srikandabala et al: Optimization and Management of DCNs: A Scoping Review

1135]

1136]

1137)

1138)

[139]

[140]

141)

[142]

[143]

1144)

1145)

[146]

47}

[148]

[149]

{150}

152]

1155]

M. Lu, Y. Gu, and D. Xie, “A dynamic and collaborative multi-layer
virtual network embedding algorithm in SDN based on reinforce-
ment learning,” JEEE Trans. Netw. Service Manage., vol. 17, no. 4,
pp. 2305-2317, Dec. 2020.

Y. Liu, F. Zhou, C. Chen, Z. Zhu, T. Shang, and J.-M. Torres-
Moreno, “Disaster protection in inter-DataCenter networks leveraging
cooperative storage.” IEEE Trans. Netw. Service Manage., vol. 18, no. 3,
pp. 2598-2611, Sep. 2021.

M. Wang, B. Cheng, and J. Chen, “Joint availability guarantee and
resource optimization of virtual network function placement in data
center networks,” /JEEE Trans. Netw. Service Manage., vol. 17, no. 2,
pp. 821-834, Jun. 2020.

S. A. Mamun, A. Ganguly, P. P. Markopoulos, A. Kwasinski, and
M. Kwon, “Security vulnerabilities of server-centric wireless datacen-
ters,” in Proc. IEEE Conf. Commun. Netw. Secur. (CNS), Jun. 2020,
pp. 1-9.

A. Ganji, A. Singh, and M. Shahzad, “Characterizing the impact of
TCP coexistence in data center networks,” in Proc. IEEE 40th Int. Conf.
Distrib. Comput. Syst. (ICDCS), Nov. 2020, pp. 388-398.

W. Li, X. Yuan, W. Qu, H. Qi, X. Zhou, 8. Chen, and R. Xu, “Efficient
coflow transmission for distributed stream processing,” in Proc. IEEE
Conf. Comput. Commun., Jul. 2020, pp. 1319-1328,

M. Macktoobian, Z. Shu, and Q. Zhao, “Traffic divergence theory:
An analysis formalism for dynamic networks,” IEEE Access, vol. 12,
pp. 67512-67524, 2024.

R-X. Hao, M-M. Gu, and JM. Chang, “Relationship between extra
edge connectivity and component edge connectivity for regular graphs,”
Theor. Comput. Sci., Vol. 833, pp. 41-55, Sep. 2020,

L. Chen, Y. Feng, B. Li, and B. Li, “A case for pricing bandwidth: Sharing
datacenter networks with cost dominant fairness,” JEEE Trans. Parallel
Distrib, Syst., vol. 32, no. 5, pp. 1256-1269, May 2021

A. Ulhassan, T. Pham, Q. Wang, and J. Stewart, “Statistical method
for multi-path interference detection in IMDD optical links,” J. Lightw.
Technol., vol. 41, no. 14, pp. 4699-4704, Jul. 15, 2023.

R. Matsumoto, R. Konoike, H. Matsuura, K. Suzuki, T. Inoue, Y. Mori,
K. Ikeda, S. Ni , and K.-I. Sato, “Design and verification of a LO
bank enabled by fixed-wavelength lasers and fast tunable silicon ring
ters for creating large scale optical switches,” Opt. Exp., vol. 29, no. 24,
p. 39930, Nov. 2021

X. Lin, S. Yue, Y. Tan, W. Sun, M. Veeraraghavan, and W. Hu, “A
partial Store-and-Forward scheduling method for inter-datacenter bulk
data transfers,” JEEE Access, vol. 8, pp. 128167—-128181, 2020.
C.Chen, J. Ye, ¥. Gao, S. Liu, and Y. Xu, “HF°T: host-based flowlet fine
tuning for RDMA load balancing,” in Proc. 8th Asia-Pacific Workshop
Nenw., Aug. 2024, pp. 9-15.

A. Althoubi, R. Alshahrani, and H. Peyravi, “Delay analysis in loT sensor
networks,” Sensors, vol. 21, no. 11, p. 3876, Jun, 2021

Y. Liang, M. Lu, Z.-J-M. Shen, and R. Tang, “Data center network design
for Internet-related services and cloud computing,” SSRN Electron. J.,
pp. 2077-2101, Jul. 2021.

V. V. Spirin, J. L. Bueno Escobedo, D. A. Korobko, P. Mégret, and
A. A, Fotiadi, “Dual-frequency laser comprising a single fiber ring cavity
for self-injection locking of DEB laser diode and Brillouin lasing,” Opt.
Exp., vol. 28, no. 25, p. 37322, Nov. 2020.

S. Hu, W. Bai, G. Zeng, Z. Wang, B. Qiao, K. Chen, K. Tan,
and Y. Wang, “Aeolus: A building block for proactive transport in
datacenters,” in Proc. Annu. Conf. ACM Special Interest Group Data
Commun. Appl., Technologies, Archit. Protocols Comput. Commun.
(SIGCOMM 20), New York, NY, USA: ACM, Aug. 2020, p. 13,
doi: 10.1145/3387514.3405878,

C. H. Song, X. Z. Khooi, R. Joshi, I. Choi, J. Li, and M. C.
Chan, “Network load balancing with in-network reordering sup-
port for RDMA,” in Proc. ACM SIGCOMM Conf., Sep. 2023,
pp. 816-831.

A. Pourhabibi, M. Sutherland, A. Daglis, and B. Falsafi, “Cerebros:
Evading the RPC tax in datacenters,” in Proc. 54th Annu. IEEE/ACM
Int. Symp. Microarchitecture, Oct. 2021, pp. 407-420.

G. Ranjan, T. N. Nguyen, H. Mekky, and Z.-L. Zhang, “On virtual
id assignment in networks for high resilience routing: A theoretical
framework,” in Proc. II Global Commun. Conf, Dec. 2020,
pp. 1-6,

Z. Xu, C. Sun, T. Ji, J. H. Manton, and W. Shieh, “Feedforward
and recurrent neural network-based transfer learning for nonlinear
equalization in short-reach optical links,” J. Lightw. Technol., vol. 39,
no. 2, pp. 475480, Jan. 15, 2021

134718

[156]

157]

[158]

[159]

[160]

(161)

[162]

1163]

[164]

[165]

[166]

167)

[168]

169}

[170]

07)

u72)

173]

174]

1175]

W-X. Liu, J. Cai, Q. C. Chen, and Y. Wang, “DRL-R: Deep rein-
forcement learning approach for intelligent routing in software~defined
data-center networks.” J. Netw. Comput. Appl., vol. 177, Mar. 2021,
Art. no. 102865.

P. Sun, Z. Guo, S. Liu, J. Lan, J. Wang, and Y. Hu, “SmartFCT: Improving
power-efficiency for data center networks with deep reinforcement
learning,” Comput, Netw., vol. 179, Oct. 2020, Art. no, 107255.

K. A. Clark, D. Cletheroe, T. Gerard, 1. Haller, K. Jozwik, K. Shi,
B. Thomsen, H. Williams, G. Zervas, H. Ballani, P. Bayvel, P. Costa,
and Z. Liu, “Synchronous subnanosecond clock and data recovery for
optically switched data centres using clock phase caching,” Nature
Electron., vol. 3, no. 7, pp. 426-433, Jun, 2020.

L. Shalev, H. Ayoub, N. Bshara, and E, Sabbag,
transport protocol for elastic and scalable HPC,
no. 6, pp. 67-73, Nov. 2020.

E Tian, Y. Zhang, W. Ye, C. Jin, Z. Wu, and Z.-L. Zhang, “Accelerating
distributed deep learning using multi-path RDMA in data center
networks,” in Proc. ACM SIGCOMM Symp. SDN Res. (SOSR), Oct. 2021,
pp. 88-100.

C. Jia, T. Pan, Z. Bian, X. Lin, E. Song, C. Xu, T. Huang, and Y. Liu,
“Rapid detection and localization of gray failures in data centers via in-
band network telemetry.” in Proc. IEEE/IFIP Netw. Operations Manage.
Symp., Apr. 2020, pp. 1-
C.K. Dominicini, G. L. Vassoler, R. Valentim, R. S. Villaca,
M.R.N. Ribeiro, M. Martinello, and E. Zambon, “KeySFC: Traffic
steering using strict source routing for dynamic and efficient network
orchestration,” Comput. Netw. vol. 167, Feb. 2020, Art. no. 106975

H, Taka, T. Inoue, and E. Oki, “Design model of a twisted and folded
clos network with multi-step grouped intermediate switches guaranteeing
admissible blocking probability.” J. Opt. Commun. Netw, vol. 16, no. 3,
p. 328, Feb, 2024.

M. Wang, B. Cheng, and J. Chen, “Joint Availability- and traffic-
aware placement of parallelized service chain in NFV-enabled data
"in Proc. IEEE Int. Conf. Web Services (ICWS), Oct. 2020,
pp. 216-223.

M. Safar, Y. Abbas, W. Iqbal, M. Y. Umair, and A. Wakeel, “ARP
overhead reduction framework for software defined data centers,” J.
Netw. Syst. Manage., vol. 30, no. 3, May 2022, Art. no. 50.

G. Suila Kuaban, B. Singh Soodan, R. Kumar, and P. Czekalski,
“Analysis of the performance of a cloud computing processing queue
with correlated reneging of tasks and resubmission,” in Proc. Int. Conf.
Electr:, Comput. Energy Technol. (ICECET), Dec. 2021, pp. 1-8.

A. Ranjith, P. Subhash, G. Nagaraju, M. Srinivas, and A, Prashanth,
“Performance study of three different types of data center network
architectures, NovaCube, BCube, and FatTree using NS-3 simulator,”
in Proc. Int. Conf. Comput. Commun. Technol. Cham, Switzerland:
Springer, 2024, pp. 411-421

M. Murakami, H. Kubokawa, K. Sugiura, E. Oki, S. Okamoto, and
N. Yamanaka, “Online parameter tuning of the flow classification method
in the energy-efficient data center network “HOLS.” J. Opt. Commun.
Netw. vol. 12, no. 11, p. 344, Nov. 2020.

X. Wu, Z. Wang, W. Wang, and T. S. E, Ng, “Augmented queue:
A scalable in-network abstraction for data center network sharing.
Proc. ACM SIGCOMM Conf., Sep. 2023, pp. 305-318.

P. Dong, X. Lu, T. Huang, L. Chen, Y. Yang, and L. Zhang, “Predictive
queue-based rate control for low latency in lossless data center networks,”
IEEE Trans. Netw. Service Manage., vol. 21, no. 3, pp. 3428-3439,
Jun, 2024.

G. Drainakis, P. Baziana, and A. Bogris, “Scalable and low server-to-
server latency data center network architecture based on optical packet
inter-rack and intra-rack switching,” J. Opt. Commun. Nenw., vol. 15,
no. 11, p. 804, Nov. 2023.

Y. Liu, W. Li, W. Qu, and H. Qi, “BULB: Lightweight and automated load
balancing for fast datacenter networks,” in Proc. 51st Int. Conf. Parallel
Process., Aug. 2022, pp. I-11.

X. Zuo, Q. Li, J. Xiao, D. Zhao, and Y. Jiang, “Drift-bottle,” in Proc. 18th
Int. Conf. Emerg. Netw. Exp. Technol., Nov. 2022, pp. 337-348

X. Tao, X. Qian, L. Han, W. Fan, Y. Shi, X. Zhu, Z. Li, S. Wei, and
R. Xu, “Key flow first prioritized flow scheduling strategy in multi-
tenant data centers,” [EEE Trans. Netw. Service Manage., vol. 21, no. 3,
pp. 3264-3277, Jun, 2024.

K. Chitavisutthivong, S. Supittayapornpong, P. Namyar, M. Zhang,
M. Yu, and R. Govindan, “Optimal oblivious routing with concave
objectives for structured networks,” /EEE/ACM Trans. Netw:, vol. 31,
no. 6, pp. 2669-2681, Dec. 2023.

cloud-optimized
IEEE Micro, vol. 40,

in

VOLUME 13, 2025



--- Page 21 ---
kK. Stikandabala et al.: Optimization and Management of DCNs: A Scoping Review

IEEE Access:

1176}

177)

[178]

[179]

[180]

181)

[182]

[183]

[184]

1185]

[186]

1187)

1188)

[189]

[190]

1191)

192)

[193]

[194]

[195]

{196}

B. Babayigit and B. Ulu, “Deep learning for load balancing of SDN-based
data center networks,” Int. J. Commun. Syst., vol. 34, no. 7, Feb. 2021,
Art. no. e4760.

F Lin, H. Wang, G. Chen, G. Zhou, T. Xu, D. Wei, L. Chen, Y. Lu,
A. Qu, H. Shao, and H. Jiang, “Fast, scalable and robust centralized
routing for data center networks,” IEEE/ACM Trans. Netw., vol. 31, n0. 6,
pp. 2624-2639, Dec. 2023.

D. De Silva and D. Alahakoon, “An artificial intelligence life cycle:
From conception to production,” Patterns, vol. 3, no. 6, Jun. 2022,
Art. no. 100489.

R. Ben Said, Z. Sabir, and I. Askerzade, “CNN-BiLSTM: A hybrid deep
learning approach for network intrusion detection system in software-
defined networking with hybrid feature selection,” IEEE Access, vol. 11,
pp. 138732—138747, 2023.
S. Satpathi, $. Deb, R. S
from network message log
pp. 1728-1741, Aug. 2019,
‘A. Mozo, B. Ordozgoiti, and S. Gémez-Canaval, “Forecasting short-term
data center network traffic load with convolutional neural networks,”
PLoS ONE, vol. 13, no. 2, Feb. 2018, Art. no. €0191939.

J. Gao, N. Yaseen, R. MacDavid, F. V. Frujeri, V. Liu, R. Bianchini,
R. Aditya, X. Wang, H. Lee, D. Maltz, M. Yu, and B. Arzani, “Scouts,”
in Proc. Annu. Conf. ACM Special Interest Group Data Commun.
Appl, Technol, Archit, Protocols Comput. Conmun., Sul. 2020,
pp. 1-21.

S. Zhang, Y. Liu, W. Meng, Z. Luo, J. Bu, S. Yang, P. Liang, D. Pei, J. Xu,
Y. Zhang, Y. Chen, H. Dong, X. Qu, and L. Song, “PreFix.” in Proc. ACM
Int. Conf. Meas. Model. Comput. Syst., Jun. 2018, pp. 1-6.

F. Yan, X. Xue, X. Guo, B. Pan, J. Wang, S. Zhang, E. Khani,
G.Guelbenzu, and N. Calabretta, “Load balance algorithm for an
OPSquare datacenter network under real application traffic.” J. Opt.
Commun. Netw, vol. 12, no. 8, p. 239, Aug. 2020.

B. Nougnanke, Y. Labit, M. Bruyere, U. Aivodji, and S. Ferlin, “ML-
based performance modeling in SDN-enabled data center network:
IEEE Trans. Netw. Service Manage. vol. 20, no. 1, pp. 815-829,
Mar. 2023.

C.Guo, L. Yuan, D. Xiang, Y. Dang, R. Huang, D. Maltz, Z. Liu, V. Wang,
B. Pang, H. Chen, Z.-W. Lin, and V. Kurien, “Pingmesh,” in Proc. ACM
Conf. Special Interest Group Data Commun., Aug. 2015, pp. 139-152.
Y. Han, J-H. Yoo, and J. W.-K. Hong, “Poisson shot-noise process
based flow-level traffic matrix generation for data center networks,”
in Proc. IFIP/EEE Int. Symp. Integr. Netw. Manage. (IM), May 2015,
pp. 450-457.

N. Lin, Q. Zhao, L. Zhao, A. Hawbani, L. Liu, and G, Min, “A novel cost-
effective controller placement scheme for software-defined vehicular
networks,” IEEE Internet Things J., vol. 8, no. 18, pp. 14080-14093,
Sep. 2021.

W. Li, Y. Jiang, X. Zhang, F. Dang, F. Gao, H. Wang, and Q. Fan,
“Reliability assurance dynamic SSC placement using reinforcement
leaning,” Information, vol. 13, no. 2, p. 53, Jan, 2022.

S. Li, Y. Qin, Z. Jiang, and W. Yang, “Efficient communication
scheduling for parameter synchronization of DML in data center
networks,” IEEE Trans. Netw. Sci. Eng., vol. 9, no. 4, pp. 1970-1985,
Jul, 2022.

Z. Guo, J. Wang, S. Liu, J. Ren, Y. Xu, and C. Yao, “Congestion-aware
critical gradient scheduling for distributed machine learning in data center
networks,” JEEE Trans. Cloud Comput., vol. 11, no. 3, pp. 2296-2311,
Jul. 2023.

P. Nallusamy, T. R. Reshmi, and M. Krishnan, “AGFT: Adaptive
entries aggregation scheme to prevent overflow in multiple flow table
environment,” Concurrency Comput, Pract. Exper, vol. 34, no. 1,
Jan, 2022, Art. no, 6491

Y. Yang, Y. Wu, Y. Jiang, and Y. Shi, “One-bit Byzantine-tolerant
distributed learning via Over-the-Air computation,” IEEE Trans. Wireless
Commun, vol. 23, no. 6, pp. 5441-5455, Jun. 2024,

X. Zhao, C. Wu, and X. Zhu, “Dynamic flow scheduling for DNN training
workloads in data centers,” IEEE Trans. Netw: Service Manage., vol. 21,
no. 6, pp. 6643-6657, Dec. 2024.

T. Wang, X. Fan, K. Cheng, X. Du, H. Cai, and Y. Wang, “Parameterized
deep reinforcement learning with hybrid action space for energy
efficient data center networks,” Comput. Nerw:, vol. 235, Nov. 2023,
Art. no. 109989.

Q. Fu, E. Sun, K. Meng, M. Li, and Y. Zhang, “Deep Q-learning for
routing schemes in SDN-based data center networks,” IEEE Access,
vol. 8, pp. 103491-103499, 2020,

kant, and H. Yan, “Learning latent events
.” IEEE/ACM Trans. Netw. vol. 27, no. 4,

VOLUME 13, 2025

1197]

[198]

[199]

[200]

Ron

[202]

[203]

[204]

[205]

[206]

[207]

[208]

[209]

(214)

J. Hu, Z. Zhou, and J. Zhang, “Lightweight automatic ECN tuning
based on deep reinforcement learning with ultra-low overhead in
datacenter networks,” JEEE Trans. Netw. Service Manage., vol. 21, no. 6,
pp. 6398-6408, Dec. 2024.

S. Abdollahi, H. Asadi, A. Montazerolghaem, and S. M. Mazinani,
“FMap: A fuzzy map for scheduling elephant flows throughjumping
traveling salesman problemvariant towardsoftware-defined networking-
baseddata center networks,” Concurrency Comput., Pract. Exper., vol. 35,
no. 26, Jun, 2023, Art. no. e7841

X. Dong, L. Nie, Z. and Y. Xiang, “Slark: A. performance
robust decentralized inter-datacenter deadline-aware coflows scheduling
framework with local information,” IEEE Trans. Parallel Distrib. Syst.,

vol. 36, no. 2, pp. I-15, Feb. 2025.
S. Abdollahi, A. Deldari, H. Asadi, A, Montazerolghaem, and
S.M. Mazinani, “Flow-aware forwarding in SDN datacenters using a

Knapsack-PSO-based solution,” IEEE Trans. Netw. Service Manage.,
vol. 18, no. 3, pp. 2902-2914, Sep. 2021

Y. Liu, J. Zhang, W. Li, Q. Wu, and P. Li, “Load balancing oriented
predictive routing algorithm for data center networks,” Future Internet,
vol. 13, no. 2, p. 54, Feb. 2021.

M. J. Abdel-Rahman, E. A. Mazied, in, K. Teague, A. B. Macken-
zie, S. F. Midkiff, K. V. Cardoso, and D. S. Nikolopoulos, “On robust
optimal joint deployment and assignment of RAN intelligent controllers
in O-RANs,” IEEE Open J. Commun, Soc., vol. 5, pp. 2358-2376,
2024.

A. Amaz, J. Lipman, M. Abolhasan, and M. Hiltunen, “Toward inte-
grating intelligence and programmability in open radio access networks:
A comprehensive survey,” IEEE Access, vol. 10, pp. 67747-67770,
2022.

C. Jiang, Y. Qiu, H. Gao, T. Fan, K. Li, and J. Wan, “An edge
computing platform for intelligent operational monitoring in Internet
data centers.” JEEE Access, vol. 7, pp. 133375-133387, 2019, doi:
10.1109/ACCESS.2019.2939614.

S. Chen, G. Zhang, S. S. Yu, Y. Mei, and Y. Zhang.
isolated bidirectional DC-DC converters for data centers,”
Electr. Eng., vol. 9, no. 4, pp. 1-22, Dec, 2023
000034,

M. M. Than, “Resource management for minimizing energy and cost
of geo-distributed data centers,” Walailak J. Sci. Technol. (WJST),
vol. 18, no. 13, Jun. 2021, Art. no. 9619, doi: 10.48048/wjst.2021.
9619.

A. Poobalan, S. Sangeetha, and P. Shanthakumar, “Optimal switching
and load distribution strategy for energy minimization and performance
optimization of cloud data center,” J. Eng. Res., vol. 43, Nov. 2021,
Art. no. 101013, doi: 10.36909/jer.13245.

A. Kellerman, “Autonomous technologies for daily personal mobili-
ties,” Eur J. Geography, vol. 14, no. 3, pp. 89-96, Aug. 2023, doi:
10.48088/ejg.a.kel.14.3.089.096.

M. Aghaei, M. Kolahi, A. Nedaei, N. S. Venkatesh, S. M. Esma
ifar, A. M. M. Sizkouhi, A. Aghamohammadi
A. Eskandari, P. Parvin, J. Milimonfared, V. Sugumaran,
Riither, “Autonomous intelligent monitoring of photovoltaic systems
An In-depth multidisciplinary review.” Prog. Photovoltaics: Res.

review of
Chin. J.
|, doi: 10.2391 9/ejee.2023,

Appl., vol. 33, no. 3, pp. 381-409, Nov. 2024, doi: 10.1002/pip.
3859.
M. S. Hoosain, B. S. Paul, S. Kass, and S. Ramakrishna, “Tools towards

the sustainability and circularity of
Sustainability, vol. 3, no. 1, pp. 173-197, Mar. 2023.
S. Mondal, F. B. Faruk, D. Rajbongshi, M. M. K. Efaz, and
M.M. Islam, “GEECO: Green data centers for energy optimization and
carbon footprint reduction,” Sustainability, vol. 15, no. 21, p. 15249,
Oct. 2023.
S. Sarkar, A. Naug, R. Luna, A. Guillén, V. Gundecha, 8. Ghorbanpour,
S. Mousavi, D, Markovikj, and A. R, Babu, “Carbon footprint reduction
for sustainable data centers in real-time,” in Proc. Conf. AAAL Artif.
Intell., Mar. 2024, vol. 38, no. 20, pp. 22322-22330.
Senthilkumar, Rajendran, Suresh, N. H. A. Rufus, R. C, Tanguturi, and
R. S. Solanki, Tanguturi, and R. $. Solanki, “Computational engineering
ce and machine learning-driven
Mach. Comput., pp. 465-474,

Circular Economy

2023.

M. Manganelli, A. Soldati, L. Martirano, and S. Ramakrishna, “Strategies
for improving the sustainability of data centers via energy mix, energy
conservation, and circular energy,” Sustainability, vol. 13, no. 11,
p. 6114, May 2021

134719


--- Page 22 ---
IEEE Access’

kK. Srikandabala et al: Optimization and Management of DCNs: A Scoping Review

[215] H. H. Mahmoud, M. Kadhim, M. Al-Shammari, I M. Hameed,
1A. Barazanchi, R. Sekhar, P. Shah, and N. Solke, “Eco-friendly and
secure data center to detection compromised devices utilizing swarm
approach,” Int. J. Innov, Eng. Sci. (IJIES), vol. 17, no. 3, pp. 102-115,
Jun, 2024.

C. Seifert, “The barriers for voluntary environmental management
systems—The case of EMAS in hospitals,” Sustainability, vol. 10, no. 5,
p. 1420, May 2018, doi: 10.3390/su 10051420.

[216]

KOGUL SRIKANDABALA (Graduate Student Member, IEEE) received
the B.Sc. degree in computer science and engineering from the University
of Moratuwa, Sri Lanka. He is currently pursuing the Ph.D. degree with
the La Trobe Business School, La Trobe University, Melbourne, Australia,
undertaking an Industry Ph.D. in partnership with NEXTDC Ltd. He is also a
Researcher with the Center for Data Analytics and Cognition (CDAC). Prior
to this, he was a Lecturer (on contract) with the Department of Computer
Science and Engineering, University of Moratuwa. His research interests
include network optimization and the application of artificial intelligence
in healthcare. His work focused on integrating data-driven methodologies
with computational intelligence to address complex optimization challenges
in healthcare and enterprise network systems.

KIRISHNNI PRABAGAR (Graduate Student Member, IEEE) received
the B.Sc. degree (Hons.) in computer science and engineering from
the University of Moratuwa, Sri Lanka, She is currently pursuing the
Ph.D. degree with La Trobe University, undertaking an Industry Ph.D.
in partnership with NEXTDC Ltd. Her research is centered on lever=
aging artificial intelligence, machine learning, and data science to drive
intelligent optimization and adaptive resource management within network
infrastructure. Before commencing her Ph.D. studies, she was a Lecturer
with the Department of Computer Science and Engineering, University
of Moratuwa. Her research interests include Al-driven optimization tech-
niques for large-scale computing environments, focusing on predictive
analytics, resource management, and intelligent automation within network
infrastructure ecosystems.

SHALINKA JAYATILLEKE is currently a Lecturer in business analytics and
artificial intelligence (AI) and the Course Coordinator of the Bachelor of
Business Analytics Degree Program, La Trobe University, and a Researcher
specializing in AI, data analytics, computer networks, and personalization,
Her work has been published in leading peer-reviewed journals and
conferences, and she has collaborated with industry and academia to
drive innovation in AL and data-driven decision-making. Her research
interests include Al-driven anomaly detection, hyper-personalization, and
conversational AI, with applications in smart grids, digital consumer
experience, and business intelligence.

134720

PEARLIE ZHANG received the B.E. degree in computer engineering and
commerce from the University of New South Wales, in 2019. In 2017,
she joined NEXTDC Ltd., where she is currently a Network Operations
‘Team Leader. Her research interests include network automation and system
integration.

RICHARD ELLERBROCK received the degree in electrical engineering from
‘Tshwane University of Technology. He is currently a Network Development
Engineer with the Network Operations Team, NEXTDC Ltd, He has more
than 30 years of global experience in data networks, communications,
security, and software and platform development in various industries,
including utilities, transport, managed services, financial services (equity
exchanges), and data centers

SEAN RINAS received the Bachelor of Electrical Engineering degree from
the University of Saskatchewan, in 1997. He is currently the Head of
Network Operations of NEXTDC Lid. With a career spanning, since 1995,
he has extensive experience in telecommunications architecture, delivery,
and operations across Canada, USA, and Austral

DASWIN DE SILVA (Senior Member, IEEE) received the Ph.D. degree in AI
from Monash University, in 2011, focused on the algorithmic development
of incremental learning without forgetting and bias. He is currently a
Professor of artificial intelligence and analytics with La Trobe University,
Australia, His expertise is in Al, algorithms, systems, applications, and
ethics. He has co-authored more than 150 research articles, received AUS
more than 14 million in industry and government funding for AI research,
and supervised 15 Ph.D.’s until completion. In the IEEE, he is the Chair of the
Technical Committee on Responsible AI, a Governing Board Member of the
IEEE Blockchain, and the IEEE Al Coalition. He is an editor of four journals
and has been consulted by the ABC News, Channel 7 News, The Australian,
Forbes, Cosmos, Times Higher Education, and The Conversation for his Al
expertise.

DAMMINDA ALAHAKOON (Member, IEEE) is currently a Professor of
business analytics and artificial intelligence and the Director of the Research
Centre for Data Analytics and Cognition, La Trobe University. His research
has been adopted in a range of domains from healthcare, utilities, smart cities,
education, industrial optimization, and national security. His work has been
published in more than 200 peer-reviewed articles and has generated more
than AUS 6 million in research and industry grants, His research is focused on
the areas of machine lean ial intelligence, advanced data analy’
business intelligence, and the harnessing of such theories for practical tools
and innovative technology for industry.

VOLUME 13, 2025

