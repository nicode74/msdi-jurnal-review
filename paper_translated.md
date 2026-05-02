IEEE Access

Received 5 June 2025, accepted 21 July 2025, date of publication 29 July 2025, date of current version 4 August 2025.

Digital Object Identifier 10, 109/ACCESS,2025.3593523

RESEARCH ARTICLE

Optimisasi dan Manajemen Jaringan Pusat Data: Tinjauan Luas tentang Tema Utama, Tantangan, serta Pendekatan Kecerdasan Buatan dan Pembelajaran Mesin

KOGUL SRIKANDABALA, (Anggota Mahasiswa Pascasarjana, IEEE),
KIRISHNNI PRABAGAR, (Anggota Mahasiswa Pascasarjana, IEEE),
SHALINKA JAYATILLEKE, PEARLIE ZHANG, RICHARD ELLERBROCK,
SEAN RINAS, DASWIN DE SILVA, (Anggota Senior, IEEE),
DAN DAMMINDA ALAHAKOON, (Anggota, IEEE)

Centre for Data Analytics and Cognition, La Trobe University, Melbourne, VIC 3086, Australia
NEXTDC Ltd., Macquarie Park, NSW 2113, Australia

Penulis korespondensi: Kogul Srikandabala (s.kogul@latrobe.edu.au)

ABSTRAK Data Center Networks (DCN) memainkan peran penting dalam memungkinkan infrastruktur digital yang skalabel, efisien, dan andal. Tinjauan luas ini menyajikan kemajuan terbaru dalam strategi optimisasi dan manajemen DCN, dengan fokus khusus pada penerapan teknik Kecerdasan Buatan (AI) dan Pembelajaran Mesin (ML). Studi ini mengikuti metodologi terstruktur yang selaras dengan protokol PRISMA-ScR dan memperluasnya dengan penggunaan Large Language Models (LLM) untuk mendukung klasifikasi tematik dan penyaringan relevansi. Analisis mengidentifikasi tujuh domain penelitian utama: jaringan optik, kontrol kemacetan, penjadwalan aliran, penyeimbangan beban, Software-Defined Networking (SDN), toleransi kesalahan, dan manajemen sumber daya hemat energi. Di dalam domain-domain ini, studi ini membandingkan pendekatan tradisional dengan metode berbasis AI yang muncul, menyoroti potensi dan keterbatasannya. Menariknya, temuan menunjukkan kurangnya kerangka kerja AI/ML terintegrasi end-to-end yang mampu menangani tuntutan multifaset dari lingkungan DCN modern. Selain itu, tinjauan ini menekankan kebutuhan akan solusi yang skalabel, dapat dijelaskan, dan sadar konteks yang selaras dengan kebutuhan DCN yang berkembang. Dengan menganalisis kumpulan pengetahuan saat ini dan menyoroti celah penelitian penting, studi ini menyediakan landasan komprehensif untuk penyelidikan masa depan ke dalam desain dan operasi DCN yang cerdas.

KATA KUNCI Kecerdasan buatan, jaringan pusat data, pembelajaran mesin, manajemen jaringan, optimisasi, software-defined networking.

1. PENDAHULUAN

Di era digital, terdapat lonjakan permintaan lalu lintas jaringan melalui layanan streaming yang menyediakan akses sesuai permintaan, platform e-commerce yang memungkinkan jutaan transaksi waktu nyata, dan jejaring sosial yang menghubungkan miliaran orang secara global dengan keterlambatan minimal dalam komunikasi. Operasi yang lancar dari layanan ini bergantung pada jaringan kompleks komputer dan perangkat keras yang saling terhubung di dalam infrastruktur berskala besar. Fasilitas-fasilitas ini menyediakan ketersediaan data, pemrosesan cepat, dan komunikasi efektif, sehingga membentuk tulang punggung Internet. Menjaga kecepatan, keandalan, dan skalabilitas infrastruktur ini menjadi semakin penting ketika masyarakat semakin bergantung pada teknologi digital. Dari menjamin konektivitas terus-menerus hingga memungkinkan pemrosesan data cepat untuk AI, layanan ini kritis bagi kemajuan teknologi modern. Fasilitas yang dikenal sebagai Pusat Data (DC) membentuk dasar komputasi dan komunikasi modern. DC menampung berbagai sumber daya komputasi yang mengumpulkan, menyimpan, berbagi, mengelola, dan mendistribusikan volume besar data. Mereka terdiri dari semua elemen fasilitas DC yang diperlukan (ruang, daya, dan pendinginan) serta elemen infrastruktur TI (server, penyimpanan, dan jaringan), berdasarkan kebutuhan bisnis [1].

DC terdiri dari berbagai komponen yang saling terhubung, di mana DCN berfungsi sebagai otak pusat. DCN adalah jaringan yang secara khusus dirancang untuk menghubungkan banyak komponen di dalam DC dan memainkan peran krusial dalam operasi sehari-hari [2]. Server dan sistem penyimpanan dalam DC hanya dapat mewujudkan potensinya sepenuhnya jika mereka dapat bertukar data dengan kecepatan sangat tinggi, menjaga latensi rendah, dan mengalami gangguan minimal. Oleh karena itu, jaringan dasar sangat penting untuk memenuhi kebutuhan operasional platform cloud, layanan streaming, dan aplikasi perusahaan. Namun, jika dibandingkan dengan jaringan komputer konvensional seperti Local Area Network (LAN), DCN menghadirkan serangkaian tantangan yang berbeda dan harus diatasi. Xia et al. menyoroti tantangan utama pada DCN, termasuk skala yang masif, ragam aplikasi yang beragam, konsumsi energi tinggi, dan kebutuhan untuk menjaga Service Level Agreement (SLA) yang ketat [2]. Studi sebelumnya telah mencoba mengatasi tantangan ini, sebagaimana diilustrasikan oleh tren penelitian yang meningkat pada Gambar 1. Namun, dalam dekade terakhir, kemajuan teknologi pada perangkat keras server didorong oleh hukum Moore [3], menghasilkan peningkatan eksponensial dalam daya pemrosesan, kapasitas memori, dan efisiensi energi. Meskipun kemampuan komputasi berkembang pesat, DCN tidak berkembang pada kecepatan yang sama. Gambar 1 menggambarkan jurang penelitian yang diamati selama bertahun-tahun. Kepadatan dan kecepatan server yang meningkat menempatkan tuntutan lebih besar pada infrastruktur jaringan; namun, arsitektur jaringan tradisional sering kesulitan mengejar, yang menyebabkan kemacetan, masalah latensi, dan transmisi data yang tidak efisien. Tantangan ini menyoroti kompleksitas yang semakin meningkat dari DCN dan menekankan perlunya penelitian dan inovasi terus menerus untuk mengatasi masalah tersebut. Meskipun kemajuan perangkat keras server sangat cepat, arsitektur dan strategi manajemen DCN tidak sejalan, menyebabkan kemacetan yang signifikan. Memahami bagaimana penelitian berkembang untuk mengatasi celah ini penting untuk mengidentifikasi area kunci untuk eksplorasi lebih lanjut.

A. SURVEI DAN TINJAUAN TERKAIT

Banyak penelitian telah meninjau berbagai aspek DCN. Tinjauan-tinjauan ini mencakup berbagai topik seperti solusi kontrol kemacetan, mekanisme manajemen lalu lintas, dan strategi optimisasi. Dengan meningkatnya kompleksitas dan skala DCN modern, peneliti berusaha memahami dan meningkatkan kinerja jaringan menggunakan metodologi dan kerangka inovatif. Banyak survei juga menyoroti munculnya AI dan ML sebagai alat yang menjanjikan untuk mengotomatisasi dan mengoptimalkan operasi DCN, membawa dimensi baru ke pendekatan manajemen jaringan tradisional.

Survei terbaru tentang DCN telah mengeksplorasi berbagai tema penting, masing-masing menangani tantangan dan kemajuan spesifik di bidang ini. Tema-tema tersebut dapat dikategorikan sebagai berikut:

- Strategi Optimisasi dalam DCN: Optimisasi jaringan tetap menjadi fokus utama banyak studi, dengan peneliti mengeksplorasi metode seperti penyeimbangan beban, rekayasa lalu lintas, dan mekanisme routing.
- Kontrol Kemacetan & Manajemen Lalu Lintas: Pertumbuhan eksponensial lalu lintas data dalam DCN menjadikan kontrol kemacetan dan manajemen lalu lintas topik penting untuk dipelajari. Beberapa survei memberikan diskusi komprehensif tentang algoritma kontrol kemacetan, teknik manajemen aliran jaringan, dan implementasinya secara praktis. Survei-survei ini membandingkan metode tradisional dengan solusi berbasis AI yang muncul, menekankan dampaknya dalam meningkatkan throughput data dan mengurangi kehilangan paket.
- Agregasi & Pemrosesan Data: Permintaan akan analitik data waktu nyata di DC besar mendorong minat yang meningkat pada teknik agregasi data. Beberapa survei menyelidiki pemrosesan dalam jaringan dan metodologi agregasi data yang meningkatkan skalabilitas dan efisiensi komputasi. Studi-studi ini fokus pada kerangka komputasi terdistribusi dan kemampuannya untuk menyederhanakan aliran data dalam jaringan berkinerja tinggi.
- Jaringan Terpadu & Kinerja Tinggi: Kemajuan perangkat keras dan perangkat lunak menghasilkan pengembangan infrastruktur jaringan terintegrasi yang menggabungkan beberapa paradigma jaringan. Survei tentang jaringan berkinerja tinggi membahas inovasi seperti interkoneksi serat optik, software-defined networking (SDN), dan network function virtualization (NFV). Studi-studi ini menelaah manfaat dan tantangan transisi ke arsitektur jaringan yang sepenuhnya terkonvergensi dan implikasinya untuk DC besar.
- Teknologi Jaringan Generasi Berikutnya: Evolusi cepat DCN mendorong penelitian ke teknologi baru yang meningkatkan skalabilitas, efisiensi, dan keamanan. Survei di domain ini mengeksplorasi DCN nirkabel, seperti jaringan 60 GHz, untuk komunikasi berkecepatan tinggi dan latensi rendah, serta strategi jaringan hemat energi untuk mengoptimalkan konsumsi daya. Studi lain fokus pada software-defined networking (SDN) dan arsitektur hiperskala yang memanfaatkan switching optik dan otomasi untuk meningkatkan kelincahan dan kinerja. Kemajuan-kemajuan ini menangani tantangan utama dalam komputasi awan dan edge, memastikan DCN tetap dapat beradaptasi dan siap menghadapi permintaan data yang terus meningkat.

Rincian lebih lanjut tentang makalah survei yang mencakup tema-tema ini dari 2010 hingga 2024 disediakan dalam Tabel 1. Tabel ini mengkategorikan upaya penelitian masa lalu dan menyoroti tren kunci dalam studi terkait DCN. Seperti yang ditunjukkan dalam Tabel 1, sementara bidang tertentu, seperti Agregasi dan Pemrosesan Data, telah menerima perhatian substansial, aspek lain, termasuk Strategi Optimisasi dalam DCN, masih relatif kurang diteliti.

Tinjauan yang ada telah memberikan wawasan berharga ke berbagai aspek optimisasi DCN, termasuk kontrol kemacetan, manajemen lalu lintas, dan teknologi jaringan generasi berikutnya. Namun, studi-studi tersebut sering kali fokus pada aspek DCN yang terisolasi daripada menawarkan sintesis komprehensif. Selain itu, meskipun peran AI/ML yang meningkat dalam optimisasi jaringan, sedikit studi yang secara sistematis menelaah penerapannya dalam manajemen DCN. Hal ini membuka peluang untuk melakukan tinjauan yang lebih terstruktur dan holistik yang mengatasi celah dalam literatur.

Beberapa survei dan tinjauan telah menelaah berbagai aspek DCN. Beberapa studi mengeksplorasi potensi AI dan ML dalam jaringan, khususnya untuk otomatisasi dan optimisasi DCN. Namun, kami mengidentifikasi celah-celah berikut dalam survei dan tinjauan tersebut:

- Fokus terlalu sempit pada aspek tertentu DCN - Sebagian besar studi hanya mencakup satu aspek DCN, seperti desain topologi jaringan, kontrol kemacetan, atau efisiensi energi. Studi-studi ini memberikan wawasan penting tetapi tidak menangkap ruang lingkup penuh penelitian DCN. Oleh karena itu, tinjauan luas yang mencakup penelitian di semua area DCN akan berguna.
- Kurangnya pendekatan tinjauan sistematis dan skoping - Di antara sedikit tinjauan yang membahas semua aplikasi dalam DCN, mayoritas mengadopsi metodologi tinjauan naratif daripada kerangka kerja sistematis atau skoping. Akibatnya, cakupannya sering kali sempit, berfokus pada teknik tertentu atau studi kasus terisolasi daripada memberikan sintesis terstruktur dari keseluruhan lanskap penelitian. Tinjauan sistematis skoping diperlukan untuk memetakan, mengkategorikan, dan menganalisis literatur yang ada, memastikan bahwa keluasan penelitian ditangkap secara memadai dan celah dalam studi DCN diidentifikasi dengan jelas.
- Analisis terbatas AI dan ML dalam optimisasi dan manajemen DCN - Meskipun penelitian tentang arsitektur dan optimisasi DCN sangat luas, sebagian besar tinjauan mengabaikan aplikasi AI/ML dalam efisiensi jaringan, manajemen lalu lintas, dan otomasi. Karena solusi berbasis AI menjadi bagian integral dari operasi jaringan, celah ini membatasi pemahaman tentang bagaimana otomatisasi cerdas dan analitik prediktif dapat meningkatkan kinerja, mengurangi konsumsi energi, dan meningkatkan keandalan.

B. KONTRIBUSI

Untuk menjembatani celah yang diidentifikasi pada Bagian I-A, studi ini menghadirkan tinjauan skoping DCN, menyediakan analisis terstruktur terhadap tema utama, metodologi, dan tren yang muncul. Dengan memasukkan diskusi berfokus pada AI/ML dan menerapkan pendekatan skoping sistematis, tinjauan ini bertujuan untuk menawarkan pemahaman komprehensif tentang bagaimana DCN dapat dioptimalkan dan dikelola secara efisien.

Kontribusi utama studi ini adalah sebagai berikut.

1. Tinjauan skoping yang dilakukan sesuai pedoman PRISMA-ScR [108], memastikan pendekatan yang sistematis dan transparan dalam meninjau penelitian DCN.
2. Pendekatan berbasis LLM yang baru untuk penyaringan dan analisis studi, memungkinkan pemodelan topik dan tinjauan literatur yang efisien dalam penelitian berskala besar di mana pemeriksaan manual tidak praktis.
3. Identifikasi dan kategorisasi tema penelitian kunci dalam DCN, memberikan wawasan tentang area fokus utama dan tren dalam bidang ini.
4. Analisis mendetail tantangan utama dalam penelitian DCN dan evaluasi solusi yang diajukan, menawarkan gambaran terstruktur tentang bagaimana peneliti mengatasi isu-isu kritis.
5. Eksplorasi konsep jaringan fundamental yang digunakan dalam penelitian DCN, menyoroti perannya dalam membentuk optimisasi jaringan dan pengembangan solusi.
6. Investigasi teknik AI/ML dalam solusi DCN, termasuk penilaian tantangan implementasi dan evaluasi komparatif terhadap pendekatan tradisional.

Dengan memetakan lanskap penelitian DCN dan mengidentifikasi celah kritis, studi ini meletakkan dasar bagi penelitian masa depan pada optimisasi jaringan berbasis AI. Sisa makalah ini disusun sebagai berikut: Bagian II menyajikan latar belakang dan motivasi untuk tinjauan ini, menetapkan konteks DCN dan pentingnya optimisasi berbasis AI. Bagian III menguraikan pertanyaan penelitian dan tujuan yang menjadi panduan tinjauan skoping ini. Bagian IV menjelaskan metodologi, termasuk strategi pencarian literatur, kriteria seleksi, dan proses ekstraksi data. Bagian V memberikan gambaran tentang konsep dasar DCN, termasuk arsitektur jaringan, protokol, dan metrik kinerja utama. Bagian VI meninjau makalah survei terkait dan menyoroti keterbatasannya, sehingga memosisikan kontribusi unik studi ini. Bagian VII memperkenalkan taksonomi baru untuk mengkategorikan penelitian tentang optimisasi DCN berbasis AI, mengorganisir studi berdasarkan area fokus dan pendekatan metodologis. Bagian VIII membahas area tematik utama yang diidentifikasi dalam literatur. Akhirnya, Bagian IX-XI menyajikan diskusi komprehensif, mensintesis wawasan utama, menguraikan tantangan saat ini, dan mengusulkan arahan penelitian masa depan.

II. METODE

Bagian ini menguraikan metodologi yang digunakan dalam tinjauan ini. Studi ini mengikuti kerangka kerja PRISMA-ScR, menggabungkan teknik manual dan otomatis untuk memastikan seleksi studi yang sistematis dan tanpa bias. Proses tinjauan meliputi perumusan pertanyaan penelitian, identifikasi dan penyaringan literatur yang relevan, penerapan kriteria inklusi dan eksklusi, serta ekstraksi data untuk analisis. Mengingat volume besar studi yang diperoleh, teknik otomasi, termasuk Large Language Models (LLM), dimanfaatkan untuk meningkatkan efisiensi, terutama dalam penyaringan tematik. Subbagian berikut memberikan rincian metodologi ini.

A. DESAIN PENELITIAN
Tinjauan skoping ini dirancang untuk menjawab pertanyaan penelitian berikut:

- RQ1 - Apa saja tema penelitian utama dalam DCN dan bagaimana mereka berkontribusi pada optimisasi dan manajemen DCN?
- RQ2 - Apa saja tantangan utama dalam setiap tema tersebut dan solusi/temuan apa yang telah diusulkan untuk mengatasinya?
- RQ3 - Konsep jaringan fundamental apa yang mendukung implementasi solusi ini, dan bagaimana mereka memungkinkan optimisasi dan manajemen DCN?
- RQ4 - Bagaimana teknik AI/ML memanfaatkan konsep jaringan untuk mengatasi tantangan DCN, dan bagaimana perbandingannya dengan pendekatan tradisional?
- RQ5 - Apa saja tantangan utama dalam merancang, mengembangkan, dan menerapkan solusi berbasis AI/ML untuk optimisasi dan manajemen DCN?

Jawaban atas pertanyaan-pertanyaan ini dibahas secara rinci pada bagian berikut.

B. IDENTIFIKASI DAN PENYARINGAN STUDI YANG RELEVAN
Proses identifikasi dan penyaringan mengikuti proses PRISMA-ScR, dan metodologinya diilustrasikan dalam Gambar 2. Pendekatan ini banyak digunakan dalam bidang medis dan biologi. Metodologi tinjauan disesuaikan untuk diterapkan dalam konteks studi ini. Metodologi ini memiliki tiga fase unik yang terjadi secara serial, seperti yang ditunjukkan dalam diagram. Pencarian komprehensif dilakukan di beberapa basis data akademik menggunakan kata kunci "Data Center Network" dan "Data Centre Network" untuk memastikan inklusivitas terminologi bahasa Inggris Amerika dan Inggris. Pencarian menghasilkan sejumlah besar studi yang kemudian diproses untuk penghapusan duplikat untuk menghilangkan redundansi. Selain itu, artikel yang tidak dapat diakses dikeluarkan agar hanya studi yang dapat diambil dan relevan yang dipertahankan untuk penyaringan lebih lanjut. Langkah ini penting untuk membangun dataset yang kuat sambil menjaga konsistensi dalam seleksi studi.

Mengingat banyaknya studi yang diperoleh, penyaringan manual semua catatan tidak memungkinkan. Meskipun beberapa kriteria objektif, seperti akses dan jenis publikasi, dapat dinilai secara andal menggunakan metadata, aspek lain, terutama relevansi tematik, memerlukan evaluasi yang lebih mendalam. Untuk memastikan efisiensi tanpa mengorbankan akurasi, diadopsi pendekatan hybrid yang menggabungkan otomasi melalui Large Language Models (LLM) dan validasi manual.

Jumlah studi yang besar dalam fase penyaringan membuat analisis manual tidak layak, sehingga otomasi diperlukan untuk identifikasi studi yang relevan secara efisien. Tujuan kami adalah menghilangkan bias sambil mencapai akurasi tingkat manusia. Large Language Models (LLM) telah banyak digunakan dalam tinjauan literatur lintas disiplin. Dennstadt menyoroti peran mereka dalam mengotomatisasi seleksi judul dan abstrak dalam penelitian biologi [109]. Mostafapour menunjukkan bagaimana LLM seperti ChatGPT membantu peneliti dengan membuat draf awal, kerangka, dan merampingkan proses tinjauan, terutama bagi mereka dengan sumber daya terbatas [110]. Hasan mengeksplorasi integrasi LLM ke dalam tinjauan sistematis, khususnya untuk penilaian risiko bias, guna meningkatkan ketelitian tinjauan [111]. Chelli lebih lanjut menekankan kemampuan LLM untuk meningkatkan pencarian literatur dan mengkonsolidasikan temuan, menjadikannya sangat berharga untuk penyaringan otomatis [112]. Studi-studi ini mengonfirmasi bahwa LLM krusial untuk mengotomatisasi dan meningkatkan proses tinjauan literatur. Mengingat skala studi dalam tinjauan skoping ini, kami memanfaatkan LLM untuk identifikasi tematik, mengurangi beban kerja manual sambil mempertahankan akurasi.

Tabel 2 merangkum kriteria seleksi yang digunakan dalam tinjauan skoping ini. Studi-studi dievaluasi berdasarkan lima kriteria utama berikut: tema utama, bahasa, jenis akses, jenis publikasi, dan jenis studi. Aplikasi otomasi bervariasi di antara kriteria penyaringan yang berbeda.

- Jenis Akses dan Jenis Publikasi: Kriteria-kriteria ini dapat dinilai secara andal menggunakan database seperti CrossRef, yang menyediakan metadata yang dapat digunakan untuk menilai apakah sebuah studi akses terbuka dan telah ditelaah sejawat. Langkah ini dapat sepenuhnya diotomasi menggunakan skrip Python.
- Bahasa dan Jenis Studi: Meskipun teknik pencocokan kata dapat mengidentifikasi studi berbahasa Inggris dan membedakan antara survei, tinjauan, dan penelitian asli, beberapa pemeriksaan manual masih diperlukan karena potensi inkonsistensi pada metadata dan klasifikasi.
- Tema Utama: Mengidentifikasi apakah sebuah studi secara eksplisit berfokus pada DCN adalah langkah yang paling menantang. Penyaringan berbasis kata kunci saja tidak cukup karena banyak studi menyebut DC tetapi tidak berfokus pada DCN. Langkah ini membutuhkan tinjauan manual. Namun, mengingat skala dataset (ribuan studi), pendekatan berbasis Large Language Model (LLM) diperlukan untuk mengotomatisasi analisis tematik sambil mengurangi upaya manusia.

Dengan mengintegrasikan API CrossRef untuk penyaringan berbasis metadata, pencocokan kata untuk klasifikasi bahasa dan jenis studi, serta LLM untuk identifikasi tematik, proses penyaringan menyeimbangkan efisiensi dan akurasi. Metode-metode otomatis ini secara signifikan mengurangi beban kerja manual sambil mempertahankan presisi penyaringan yang tinggi. Dengan dataset akhir terkurasi, langkah selanjutnya adalah mengekstraksi wawasan kunci dari studi yang dipilih.

Tujuh tema utama diekstraksi dari makalah yang difilter, yang secara kolektif mewakili berbagai area fokus yang diselidiki oleh penelitian yang dipublikasikan di domain DCN.

III. TEMA PENELITIAN UTAMA

Tema-tema utama yang diidentifikasi dalam literatur adalah sebagai berikut:

- Jaringan Optik dan Transmisi Kecepatan Tinggi (N=328, 20%): Dengan pertumbuhan eksponensial permintaan lalu lintas data, Jaringan Optik menjadi solusi yang menawarkan laju transmisi ultra-cepat, latensi rendah, dan konsumsi daya lebih rendah.
- Kontrol Kemacetan dan Optimisasi Latensi (N=233, 14%): Seiring dengan transmisi kecepatan tinggi, muncul tantangan mengelola kemacetan jaringan dan mengurangi latensi. Mekanisme kontrol kemacetan penting untuk mencegah kehilangan paket, meminimalkan penundaan, dan mengoptimalkan aliran lalu lintas di seluruh jaringan.
- Penjadwalan Aliran dan Jaringan Sadar Tenggat Waktu (N=216, 13%): Tidak semua lalu lintas jaringan sama; beberapa aplikasi membutuhkan latensi rendah dan tenggat waktu yang dijamin. Penjadwalan aliran digunakan untuk memastikan alokasi sumber daya jaringan yang efisien dengan memprioritaskan beban kerja kritis dan tenggat waktu berbasis aplikasi.
- Penyeimbangan Beban dan Distribusi Lalu Lintas (N=123, 8%): Penjadwalan aliran yang efektif menciptakan kebutuhan untuk penyeimbangan beban guna mengoptimalkan pemanfaatan sumber daya agar lalu lintas jaringan tersebar secara merata, sehingga mencegah pemanfaatan berlebih dan pemanfaatan kurang.
- Software-Defined Networking (SDN) dan Kontrol Lalu Lintas (N=198, 12%): Evolusi teknik penyeimbangan beban membutuhkan mekanisme kontrol lalu lintas yang dapat diprogram dan fleksibel. SDN memungkinkan manajemen jaringan tersentralisasi, rekayasa lalu lintas dinamis, dan penyesuaian kebijakan secara waktu nyata.
- Toleransi Kesalahan dan Ketahanan Jaringan (N=250, 15%): Implementasi SDN membawa tantangan baru dalam memastikan keandalan jaringan. Mekanisme toleransi kesalahan meningkatkan ketahanan jaringan dengan menerapkan strategi redundansi, pemulihan kegagalan, dan teknik pemeliharaan prediktif.
- Manajemen Sumber Daya Hemat Energi dan Cloud (N=288, 18%): Mengoptimalkan kinerja jaringan tidak lengkap tanpa menangani keberlanjutan. Strategi hemat energi menjaga keberlanjutan dengan mengoptimalkan konsumsi daya di lingkungan cloud berskala besar.

Bagian-bagian berikut mensintesis studi yang difilter, dikategorikan berdasarkan tema mereka, untuk mengekstraksi wawasan bermakna tentang tantangan yang mendorong penelitian, kontribusi yang dibuat oleh penelitian tersebut, tren yang muncul, dan efektivitas berbagai solusi yang diusulkan. Gambar 3 menyajikan analisis kuantitatif distribusi tema di antara faktor-faktor ini.

Diskusi RQ1
Apa saja tema penelitian utama dalam DCN dan bagaimana mereka berkontribusi pada optimisasi dan manajemen DCN?

Tema utama dalam penelitian DCN adalah tujuh tema yang disebutkan di atas. Bersama-sama, tema-tema tersebut menyediakan dasar bagi studi dan inovasi DCN saat ini. Dengan mengatasi isu penting dalam hal kecepatan, efisiensi, adaptabilitas, dan keandalan, tema-tema utama ini dapat membantu mengoptimalkan dan mengelola DCN. Sementara kontrol kemacetan dan optimisasi latensi menjamin aliran lalu lintas jaringan yang tidak terganggu dari titik kemacetan, jaringan optik menjamin transfer data berkecepatan tinggi dalam DCN. Beban kerja kritis diprioritaskan dalam penjadwalan aliran dan jaringan sadar tenggat waktu, sehingga meningkatkan kualitas layanan. Penyeimbangan beban dan distribusi lalu lintas mengoptimalkan penggunaan sumber daya untuk mencegah kelebihan beban sistem. Sementara toleransi kesalahan dan ketahanan jaringan meningkatkan keandalan dengan mengurangi gangguan layanan, software-defined networking (SDN) dan manajemen lalu lintas menambahkan kemampuan pemrograman dan fleksibilitas, memungkinkan penyesuaian lalu lintas waktu nyata. Terakhir, manajemen sumber daya cloud hemat energi menjamin keberlanjutan dengan menurunkan biaya operasional dan konsumsi daya. Secara keseluruhan, komponen-komponen ini menentukan arah strategis di mana DCN akan berkembang.

IV. DAYA PENDORONG OPTIMISASI DCN: TANTANGAN DI ANTARA TEMA UTAMA

Berdasarkan tinjauan tematik yang disajikan di Bagian III, bagian ini menggali lebih dalam setiap dari tujuh tema penelitian dengan memeriksa secara sistematis tantangan kunci, motivasi dasar, dan isu yang belum terselesaikan yang mendorong upaya optimisasi berkelanjutan dalam penelitian DCN.

Evolusi DCN didorong oleh tantangan seperti skalabilitas, kemacetan, risiko keamanan, dan konsumsi energi. Tantangan-tantangan ini berfungsi sebagai faktor pendorong yang membentuk tujuan penelitian DCN. Bagian ini mengeksplorasi kekuatan pendorong utama di balik optimisasi DCN dan memeriksa tujuannya, motivasi, dan tantangan di seluruh tujuh tema fundamental yang diekstraksi dari literatur.

Jaringan Optik dan transmisi berkecepatan tinggi merupakan kunci untuk memastikan aliran data yang mulus dalam DCN. Arsitektur tradisional kesulitan mengimbangi peningkatan lalu lintas data, sehingga muncul kebutuhan akan rekayasa lalu lintas cerdas, komponen optik hemat energi, dan mekanisme keamanan yang tangguh. Penelitian telah fokus pada rekayasa lalu lintas berbasis AI, optimisasi lalu lintas multilapis, dan kontrol kemacetan prediktif berbasis ML untuk meningkatkan kinerja jaringan [113], [114]. Kemajuan dalam komponen optik hemat energi bertujuan mengurangi biaya operasional, sementara mekanisme enkripsi dan toleransi kesalahan memperkuat keamanan dan ketahanan jaringan [115].

Kontrol Kemacetan dan Optimisasi Latensi penting untuk transmisi yang dapat diandalkan dalam DCN. Namun, mekanisme kontrol kemacetan statis kesulitan beradaptasi dengan kondisi lalu lintas dinamis, sehingga menyebabkan hambatan kinerja dan latensi. Tantangan ini menciptakan kebutuhan akan optimisasi transportasi adaptif dan proaktif untuk meningkatkan responsivitas jaringan.

Penelitian telah berfokus pada masalah ini melalui teknik kontrol kemacetan adaptif [116] yang menyesuaikan aliran lalu lintas secara dinamis untuk mencegah kemacetan. Pengurangan latensi dapat diatasi dengan menerapkan strategi transportasi prediktif dan proaktif [117] serta pendekatan berbasis kredit dan RTT [118].

Penjadwalan Aliran dan Jaringan Sadar Tenggat Waktu sangat penting untuk mengelola beban lalu lintas yang meningkat dalam DCN. Seiring beban lalu lintas terus meningkat, memastikan transmisi latensi rendah dan sadar tenggat waktu sangat penting untuk mendukung lalu lintas prioritas tinggi dan real-time. Tantangan ini menciptakan kebutuhan akan penjadwalan lalu lintas yang efisien dan klasifikasi aliran yang akurat untuk mengoptimalkan kinerja jaringan. Untuk memenuhi kebutuhan ini, penelitian telah mengeksplorasi penjadwalan berbasis prioritas, klasifikasi aliran adaptif, dan alokasi sumber daya dinamis sebagai solusi utama [119], [120], [121] untuk meningkatkan efisiensi aliran dan memastikan tugas kritis memenuhi tenggat waktunya.

Penyeimbangan Beban dan Distribusi Lalu Lintas penting untuk mengelola pertumbuhan lalu lintas jaringan, mencegah kemacetan dan ketidakseimbangan beban, sehingga menciptakan kebutuhan akan strategi routing yang efisien. Strategi routing berbasis OpenFlow telah diselidiki untuk mendeteksi dan mengurangi aliran gajah serta meningkatkan skalabilitas dan distribusi lalu lintas [122]. Teknik migrasi switch dalam kontroler SDN juga telah dieksplorasi untuk mengurangi kemacetan secara dinamis dan meningkatkan penyeimbangan beban [123]. Studi tentang penyeimbangan beban multipath terdistribusi dinamis telah memperkenalkan strategi untuk memastikan operasi jaringan tetap tidak terganggu selama kegagalan [124]. Selain itu, penelitian telah fokus pada penciptaan mekanisme penyeimbangan beban adaptif untuk meminimalkan pengurutan ulang paket dan mengoptimalkan QoS [125].

Software-Defined Networking (SDN) dan Kontrol Lalu Lintas muncul sebagai pendekatan fundamental untuk mengelola kompleksitas yang berkembang dari Data Center Networks (DCN). Seiring volume lalu lintas melonjak dan tuntutan aplikasi menjadi semakin dinamis, arsitektur jaringan tradisional menghadapi keterbatasan dalam hal skalabilitas, kemampuan pemrograman, dan adaptabilitas. SDN mengatasi masalah ini dengan memisahkan kontrol plane dan data plane, sehingga memungkinkan kontrol terpusat dan dapat diprogram atas perilaku jaringan. Namun, pergeseran arsitektural ini memperkenalkan tantangan baru, termasuk penempatan kontroler yang optimal, skalabilitas control plane, dan integrasi model SDN hibrida. Isu-isu ini menjadi fokus penelitian yang mengeksplorasi kerangka pemantauan berbasis telemetri, dataset tahan intrusi, dan arsitektur RPC yang dioptimalkan untuk mendukung penerapan SDN yang efisien dan tangguh [126], [127], [128]. Selain itu, kontrol lalu lintas dalam SDN harus menghadapi ancaman keamanan yang muncul. Studi telah menunjukkan efektivitas model pembelajaran mesin terawasi seperti SVM, K-Nearest Neighbors, dan Decision Trees untuk klasifikasi lalu lintas waktu nyata yang akurat dan deteksi serangan DDoS dalam lingkungan SDN emulasi [129], [130]. Kemajuan lebih lanjut dalam arsitektur berbasis AI dan Moving Target Defense (MTD) menawarkan perlindungan tambahan untuk plane kontrol dan data yang rentan [131]. Secara kolektif, inovasi-inovasi ini memperkuat peran SDN dalam membentuk DCN yang skalabel, cerdas, dan aman yang mampu mendukung tuntutan throughput tinggi dan latensi rendah dalam lingkungan pusat data yang berubah.

Toleransi Kesalahan dan Ketahanan Jaringan penting untuk memastikan keandalan dan stabilitas DCN. Namun, kerusakan jaringan, kegagalan yang tidak terdeteksi, dan masalah keandalan terus menimbulkan risiko bagi jaringan. Terjadinya kegagalan yang tidak terduga dalam infrastruktur edge computing memerlukan strategi prediksi dan mitigasi kegagalan lanjutan untuk meminimalkan gangguan layanan [132]. Kekhawatiran biaya dan efisiensi energi diatasi dengan mengoptimalkan arsitektur jaringan dan mengurangi ketergantungan pada tautan kabel yang mahal, sehingga meningkatkan ketahanan terhadap kesalahan dan mengurangi biaya operasional [133]. Tantangan-tantangan ini menciptakan kebutuhan akan mekanisme toleran kesalahan cerdas, jaringan yang mampu menyembuhkan diri sendiri, dan strategi pemulihan kegagalan hemat energi.

Manajemen Sumber Daya Hemat Energi dan Cloud sangat penting dalam mengoptimalkan operasi DC di tengah berbagai tantangan. DC mengonsumsi energi dalam jumlah besar, menyebabkan biaya operasional yang tinggi dan dampak lingkungan, yang menciptakan tantangan efisiensi biaya dan energi [134]. Manajemen sumber daya jaringan tradisional kesulitan mengalokasikan sumber daya secara dinamis untuk mengakomodasi bebab kerja yang makin berkembang, menyebabkan tantangan skalabilitas dan kinerja [135]. Kekhawatiran tentang keandalan, ketahanan, dan keamanan menciptakan kebutuhan akan solusi untuk mengurangi kegagalan, ancaman siber, dan bencana yang dapat mengompromikan ketersediaan layanan [136]. Tantangan-tantangan ini memerlukan alokasi sumber daya yang cerdas dan sadar energi, distribusi beban kerja adaptif, dan strategi manajemen cloud yang aman untuk meningkatkan keberlanjutan dan kinerja [137].

V. KONSEP DASAR DAN KEMAJUAN UTAMA DALAM DCN

Tantangan yang mendorong penelitian DCN telah menghasilkan kontribusi signifikan di tujuh tema dalam DCN. Kontribusi-kontribusi ini dapat dibagi menjadi lima kategori: kerangka konseptual, inovasi metodologis, kemajuan arsitektural, peningkatan algoritmik, dan pengembangan teknologi. Bagian ini mengeksplorasi kontribusi utama tersebut, menyoroti solusi penting yang telah mengubah DCN dan meletakkan dasar bagi penelitian masa depan.

A. KERANGKA KONSEPTUAL

Kerangka konseptual (N=52, 3%) memperkenalkan teori baru, paradigma, dan model dasar yang membentuk penelitian jaringan masa depan. Secara kolektif, kontribusi-kontribusi ini memberikan landasan teoretis yang kuat untuk meningkatkan efisiensi DCN.

Dalam jaringan optik, identifikasi ancaman keamanan kritis dalam jaringan optik nirkabel merupakan kemajuan konseptual penting yang membantu menyoroti kerentanan untuk transmisi data berkecepatan tinggi yang aman [138]. Kontrol kemacetan memperkenalkan studi konseptual komprehensif tentang koeksistensi TCP dan efeknya terhadap lalu lintas DC modern, menyediakan wawasan penting tentang bagaimana protokol jaringan berinteraksi, serta membantu membentuk strategi routing yang lebih cerdas [139]. Penjadwalan aliran dan jaringan sadar tenggat waktu telah meningkat secara signifikan dengan diperkenalkannya konsep metrik coflow age (CA), yang meningkatkan penjadwalan prioritas untuk aplikasi sensitif latensi [140]. Dalam kontrol SDN, inovasi konseptual paling signifikan adalah pengembangan teori divergensi lalu lintas, yang meningkatkan pemahaman tentang aliran lalu lintas jaringan dan memungkinkan mekanisme kontrol berbasis SDN yang lebih efisien [141]. Pemahaman teoretis tentang bagaimana konektivitas pinggiran ekstra memperkuat ketahanan jaringan dan membantu penyembuhan diri telah meningkatkan pemahaman kita tentang daya tahan jaringan [142].

Demikian pula, pengenalan konsep fairness dominan biaya untuk alokasi bandwidth merupakan terobosan besar dalam mengoptimalkan distribusi sumber daya di infrastruktur cloud [143].

B. INOVASI METODOLOGIS

Inovasi metodologis (N=82, 5%) berfokus pada penyempurnaan metodologi penelitian, teknik validasi, kerangka keamanan, dan strategi pengujian kinerja.

Inovasi kunci dalam jaringan optik meliputi metodologi desain bank panjang gelombang, yang secara sistematis meningkatkan efisiensi spektral, dan metodologi deteksi sinyal berbasis DSP, yang memberikan pendekatan terstruktur untuk mengidentifikasi kesalahan transmisi [144]. Demikian pula, metodologi yang mengintegrasikan model MPTCP kooperatif dan teknik reinforcement learning diperkenalkan untuk mengelola lalu lintas jaringan secara efisien, mencegah kemacetan, dan menyesuaikan aliran data secara waktu nyata guna mengurangi penundaan [145]. Dalam penjadwalan aliran, metode penjadwalan store-and-forward baru dibuat untuk memanfaatkan bandwidth lebih baik dan mengurangi penundaan pemrosesan pada aplikasi sensitif waktu [146]. Dalam penyeimbangan beban dan manajemen lalu lintas, metodologi HF?T telah meningkatkan distribusi lalu lintas jaringan, membuatnya lebih efisien dalam lingkungan yang berubah [147]. Kontribusi penting terhadap mekanisme toleran kesalahan meliputi metodologi yang melibatkan model antrean dua tahap yang diperkenalkan untuk memprediksi keterlambatan jaringan, menjadikan jaringan lebih tahan terhadap kegagalan [148]. Kebaruan penting lainnya adalah pengenalan model matematika baru untuk membantu mendistribusikan sumber daya lebih efektif, sehingga mengurangi biaya sambil mempertahankan kinerja komputasi cloud hemat energi [149].

C. KEMAJUAN ARSITEKTURAL

Kemajuan arsitektural (N=479, 29%) berfokus pada desain jaringan, topologi, serta infrastruktur fisik/logis. Kontribusi-kontribusi ini sering melibatkan struktur routing baru dan perubahan tingkat sistem yang mengubah cara jaringan disusun secara fisik dan logis.

Arsitektur hibrida optik-nirkabel yang terintegrasi dengan software-defined optical networking meningkatkan kemampuan adaptasi bandwidth dan kecepatan transmisi [150]. Kerangka kerja seperti sistem kontrol kemacetan berbasis RTT & sistem penjadwalan paket berkecepatan tinggi [151] meminimalkan kemacetan dan mengurangi latensi. Arsitektur seperti antrean FIFO tunggal AIFO dan penjadwalan multi-layer yang sadar prioritas meningkatkan prioritisasi lalu lintas dan transmisi sadar tenggat waktu [119]. Kerangka kerja seperti ConWeave memperkenalkan sistem rerouting granular yang meningkatkan penyeimbangan beban pada jaringan berbasis RDMA [152]. Arsitektur SDN menggunakan prosesor RPC khusus untuk mikroservis, yang mengoptimalkan latensi dan kinerja di lingkungan komputasi terdistribusi [153]. Arsitektur jaringan toleran kesalahan hierarkis telah dibuat untuk meningkatkan mekanisme pemulihan kegagalan dan memperkuat ketahanan DCN [154]. Arsitektur migrasi beban kerja berbasis AI, embedding jaringan virtual hemat biaya, dan penjadwalan sadar energi mengurangi konsumsi daya dan mengoptimalkan pemanfaatan infrastruktur cloud [134].

D. PENINGKATAN ALGORITMIK

Peningkatan algoritmik (N=749, 46%) melibatkan pengembangan algoritme cerdas dan teknik untuk mengoptimalkan fungsi jaringan. Kontribusi-kontribusi ini terdiri dari teknik komputasi maju yang memengaruhi proses jaringan dan mengoptimalkan pengambilan keputusan.

Algoritme transfer learning telah diusulkan untuk meningkatkan prediksi kegagalan tautan dan kinerja jaringan dalam sistem optik berkecepatan tinggi [155]. Mekanisme kontrol kemacetan PI yang dapat menyetel sendiri menyesuaikan ukuran jendela secara dinamis untuk beradaptasi dengan kondisi jaringan yang berubah dan meminimalkan kemacetan [116]. Strategi penjadwalan granular telah dibuat untuk memprioritaskan aplikasi sensitif latensi, memastikan alokasi bandwidth yang efisien [119]. Algoritme migrasi switch yang sangat efisien mengoptimalkan beban kerja kontroler, memastikan aliran lalu lintas seimbang di jaringan berbasis SDN [123]. Mekanisme kontrol lalu lintas berbasis SDN yang canggih dengan routing berbasis DRL memungkinkan kontrol lalu lintas adaptif yang mengurangi kemacetan dan meningkatkan pengiriman paket [156]. Algoritme yang memanfaatkan deep reinforcement learning (DRL) telah digunakan untuk menciptakan jaringan yang mampu menyembuhkan diri, secara signifikan meningkatkan prediksi dan pemulihan kegagalan [132]. Strategi alokasi sumber daya baru (algoritme BFS yang dimodifikasi) dan strategi penempatan VM adaptif telah diusulkan untuk menjadwalkan tugas secara efektif di lingkungan komputasi cloud dan mengoptimalkan pemanfaatan sumber daya sambil mempertahankan standar QoS [134].

E. PENGEMBANGAN TEKNOLOGI

Inovasi teknologi (N=274, 17%) melibatkan perangkat keras baru, perangkat jaringan, teknologi transmisi dan komunikasi, serta kemajuan perangkat lunak.

Kontribusi teknologi utama dalam jaringan optik adalah penggunaan frekuensi ganda untuk meningkatkan stabilitas komunikasi optik. Clock phase caching memungkinkan pemulihan sub-nanodetik dalam jaringan optik. Selain itu, format modulasi canggih meningkatkan efisiensi transmisi data optik [157], [158]. Protokol Scalable Reliable Datagram (SRD), sebuah peningkatan komunikasi yang baru dirancang, dibuat untuk meningkatkan kinerja komunikasi [159]. Teknologi SmartFCT memanfaatkan deep reinforcement learning (DRL) dengan SDN untuk memungkinkan manajemen lalu lintas waktu nyata [157]. Solusi multipath RDMA berbasis perangkat lunak dengan sistem nyata, Maestro, diusulkan untuk meningkatkan efisiensi distribusi beban [160]. Kontribusi signifikan lainnya adalah In-band Network Telemetry (INT), sebuah sistem aktif untuk deteksi kegagalan abu-abu secara waktu nyata, yang menjadi solusi ketahanan jaringan yang dapat diterapkan langsung [161]. KeySFC mengintegrasikan SDN dengan routing sumber ketat, memberikan solusi jaringan teroptimalkan, skalabel, dan hemat energi [162].

Diskusi RQ2
Apa saja tantangan utama dalam setiap tema ini?

Tantangan utama dalam penelitian DCN dapat dikategorikan ke dalam area kunci:

- Tantangan skalabilitas, kemacetan, latensi, keamanan, toleransi kesalahan, dan efisiensi energi akibat meningkatnya lalu lintas data dan arsitektur yang kompleks.
- Jaringan optik berkecepatan tinggi, kontrol kemacetan adaptif, deteksi anomali, manajemen lalu lintas cerdas, manajemen sumber daya hemat energi, migrasi beban kerja, dan solusi jaringan hijau sangat penting untuk mengatasi masalah ini.

Solusi/terobosan apa yang telah diusulkan untuk mengatasinya?

Untuk mengatasi tantangan ini, penelitian DCN telah memperkenalkan perbaikan arsitektural (jaringan hibrida, topologi toleran kesalahan), optimisasi algoritmik (pembelajaran mendalam untuk kontrol lalu lintas, prediksi kegagalan), inovasi teknologi (telemetri jaringan in-band, penjadwalan berkecepatan tinggi), dan penyempurnaan metodologis (pemodelan lalu lintas, strategi kemacetan). Kontribusi-kontribusi ini meningkatkan kinerja, keamanan, dan keberlanjutan, memastikan DCN yang skalabel dan tangguh.

VI. PRINSIP JARINGAN INTI DALAM DCN

Kemajuan dalam penelitian DCN bergantung pada fondasi kuat dari konsep jaringan. Untuk memungkinkan operasi DCN yang cerdas dan adaptif, peneliti telah fokus pada tiga konsep kunci: Pemodelan, Deteksi Anomali, dan Representasi.

A. PEMODELAN DAN REPRESENTASI

Representasi dalam DCN melibatkan pemodelan struktur jaringan, aliran lalu lintas, dan perilaku sistem untuk analisis, simulasi, dan optimisasi routing. Model-model ini menjadi dasar bagi solusi DCN lanjut.

Peningkatan representasi jaringan menghasilkan kinerja yang lebih baik. Dalam [163], model matematis untuk jaringan Clos dikembangkan untuk mengoptimalkan topologi DC. Demikian pula, [152] fokus pada simulasi perilaku Remote Direct Memory Access (RDMA) untuk menganalisis dampaknya terhadap kinerja jaringan.

Pembelajaran representasi jaringan juga dieksplorasi untuk berbagai aplikasi, termasuk optimisasi lalu lintas dan deteksi anomali. Misalnya, dalam [124], topologi leaf-spine digunakan untuk secara efisien menyusun data DCN, sehingga cocok untuk analisis jaringan berbasis AI. Studi lain [125] memanfaatkan pembelajaran representasi untuk mengoptimalkan protokol routing dan mengurangi pengurutan ulang paket, yang mengarah pada transmisi data yang lebih efisien.

B. PROFILING PERILAKU JARINGAN

Profiling penting untuk memahami pola lalu lintas, perilaku jaringan, dan pemanfaatan sumber daya, sehingga memungkinkan penerapan strategi manajemen DCN adaptif. Teknik profiling telah digunakan untuk mengoptimalkan kinerja DCN. Penelitian dalam [123] menerapkan teknik profiling untuk menganalisis lalu lintas jaringan dan meningkatkan strategi migrasi switch dalam Software-Defined Networking (SDN). Demikian pula, dalam [122], metode profiling digunakan untuk mensimulasikan perilaku jaringan, memungkinkan distribusi lalu lintas dan efisiensi yang lebih baik. Studi lain, [125], memanfaatkan profiling untuk menilai pengurutan ulang paket, yang penting untuk memastikan Quality of Service (QoS) dalam DCN. Teknik profiling berbasis AI semakin populer. Dalam [124], model ML digunakan untuk mengklasifikasikan aliran jaringan secara dinamis, meningkatkan alokasi sumber daya.

C. DETEKSI ANOMALI DAN ANCAMAN KEAMANAN

Deteksi anomali merupakan komponen kritis dari keamanan DCN dan manajemen kinerja untuk mengidentifikasi ancaman, salah konfigurasi, dan kegagalan yang memengaruhi stabilitas jaringan.

Dengan meningkatnya kompleksitas DC modern, mendeteksi anomali dalam perilaku jaringan normal dapat membantu mengurangi ancaman keamanan, salah konfigurasi, dan kegagalan. Dalam [164], model deteksi anomali berbasis AI dikembangkan untuk mendeteksi aktivitas berbahaya di lingkungan virtualisasi. Demikian pula, dalam [165], model pembelajaran mendalam dilatih pada data kontroler SDN untuk meningkatkan pemantauan keamanan.

Deteksi anomali juga memainkan peran penting dalam pertahanan terhadap ancaman siber, seperti serangan Distributed Denial-of-Service (DDoS). Penelitian dalam [166] fokus pada pemantauan lalu lintas waktu nyata untuk mendeteksi tanda-tanda awal serangan DDoS dan mencegah gangguan skala besar. Studi lain [167] menggabungkan metode statistik dengan telemetri jaringan untuk mendeteksi anomali lalu lintas di DCN berbasis cloud, sehingga meningkatkan keandalan jaringan.

D. SALING KETERGANTUNGAN REPRESENTASI, PROFILING, DAN DETEKSI ANOMALI

Representasi membentuk dasar dengan menyediakan model terstruktur perilaku jaringan. Profiling membangun dari sini dengan menganalisis pola lalu lintas dan penggunaan sumber daya serta mengekstraksi wawasan berarti untuk optimisasi. Deteksi anomali bergantung pada representasi dan profiling untuk mengidentifikasi penyimpangan, mendeteksi ancaman, dan meningkatkan keamanan. Ketiga konsep ini menciptakan umpan balik berkelanjutan: representasi menyusun data, profiling menginterpretasikannya, dan deteksi anomali memurnikannya dengan mengidentifikasi keanehan. Integrasi mereka memungkinkan manajemen DCN yang cerdas, adaptif, dan otomatis untuk meningkatkan efisiensi serta keamanan.

Diskusi RQ3
Konsep jaringan fundamental apa yang mendukung implementasi solusi ini, dan bagaimana mereka memungkinkan optimisasi dan manajemen DCN?

Konsep kunci adalah Representasi, Profiling, dan Deteksi Anomali.

Representasi menyusun perilaku jaringan untuk optimisasi lalu lintas, efisiensi routing, dan analisis berbasis AI. Profiling memeriksa pola lalu lintas dan penggunaan sumber daya serta meningkatkan kinerja, penyeimbangan beban, dan alokasi sumber daya adaptif. Deteksi Anomali mengidentifikasi ancaman keamanan, kegagalan, dan salah konfigurasi, membantu deteksi intrusi, mitigasi DDoS, dan pemantauan waktu nyata. Konsep-konsep ini saling terkait, dengan representasi memberikan struktur, profiling mengekstrak wawasan, dan deteksi anomali memurnikan keduanya, memungkinkan operasi DCN yang cerdas, skalabel, dan aman.

VII. ANALISIS PERBANDINGAN ANTARA TEKNIK JARINGAN TRADISIONAL DAN BERBASIS AI

DCN telah berkembang secara signifikan, bergeser dari teknik statis berbasis aturan ke solusi adaptif berbasis AI. Meskipun metode tradisional memberikan stabilitas dan efisiensi, solusi AI/ML menawarkan kemampuan adaptasi lebih tinggi, kemampuan prediktif, dan otomasi. Bagian ini membandingkan kedua pendekatan dan menyoroti keunggulan, keterbatasan, dan tren yang muncul.

A. TEKNIK KONVENSIONAL DALAM DCN

Metode DCN tradisional (N=1371, 84%) bergantung pada aturan yang telah ditetapkan, heuristik, dan model statis untuk mengoptimalkan operasi jaringan. Teknik-teknik ini telah banyak digunakan untuk berbagai fungsi jaringan, tetapi sering kekurangan fleksibilitas yang dibutuhkan untuk beradaptasi dengan fluktuasi jaringan waktu nyata.

Jaringan optik umumnya menerapkan strategi penetapan panjang gelombang tetap untuk memastikan jalur transmisi yang stabil. Namun, metode ini gagal menyesuaikan secara waktu nyata berdasarkan kondisi tautan, sehingga menjadi tidak efisien pada jaringan adaptif [168]. Demikian pula, mekanisme kontrol kemacetan seperti TCP Reno dan TCP Cubic hanya bereaksi setelah kemacetan terjadi, menyebabkan masalah skalabilitas pada infrastruktur DCN besar [169].

Untuk mendistribusikan lalu lintas, algoritme penjadwalan dan manajemen antrean seperti round-robin scheduling dan weighted fair queuing mengalokasikan sumber daya secara adil tetapi kurang responsif terhadap lonjakan lalu lintas mendadak [122], [123]. Demikian juga, manajemen aliran SDN berbasis aturan mengarahkan lalu lintas melalui jalur yang telah ditentukan, memberikan kontrol tetapi tidak memiliki adaptabilitas waktu nyata [152], [170].

Dalam hal toleransi kesalahan, teknik berbasis failover dan redundansi memastikan stabilitas jaringan, tetapi memperkenalkan overhead tambahan dan biaya infrastruktur [124], [125]. Demikian pula, strategi manajemen daya statis di lingkungan cloud mengoptimalkan konsumsi energi di bawah kondisi stabil tetapi kesulitan menghadapi beban kerja dinamis, sehingga menyebabkan pemanfaatan sumber daya yang tidak efisien [122].

Metode tradisional memberikan stabilitas, biaya komputasi rendah, dan kemudahan implementasi. Namun, ketergantungan mereka pada representasi statis untuk struktur jaringan, profiling berbasis aturan untuk pemantauan lalu lintas, dan deteksi anomali berbasis tanda tangan membuat mereka kurang adaptif terhadap fluktuasi waktu nyata dan otomasi berskala besar, sehingga mengurangi efektivitasnya dalam lingkungan dinamis.

B. PENDEKATAN BERBASIS AI DAN ML DALAM DCN

Teknik berbasis AI/ML (N=265, 16%) mengubah manajemen DCN dengan memungkinkan pengambilan keputusan waktu nyata, analisis prediktif, dan kemampuan pembelajaran mandiri. Tidak seperti pendekatan berbasis aturan statis, solusi berbasis AI menyesuaikan diri secara dinamis terhadap kondisi jaringan, memprediksi kemacetan, dan mengoptimalkan alokasi sumber daya.

Dalam jaringan optik berkecepatan tinggi, model AI meningkatkan keandalan transmisi dengan mengoptimalkan modulasi sinyal dan memprediksi kegagalan tautan [171]. Demikian pula, kontrol kemacetan berbasis AI memungkinkan manajemen aliran lalu lintas proaktif, sehingga mencegah hambatan sebelum terjadi [172]. Model AI memanfaatkan Representasi untuk menyusun data jaringan secara efisien.

AI/ML juga meningkatkan penjadwalan waktu nyata dan penyeimbangan beban, menyesuaikan lalu lintas jaringan secara dinamis dan memprioritaskan tugas berdasarkan data serta kondisi jaringan waktu nyata. Algoritme Deep Deterministic Policy Gradient (DDPG) dan Deep Reinforcement Learning mengoptimalkan bobot tautan dan pola lalu lintas, memastikan distribusi beban yang efisien [173]. Selain itu, kontroler SDN berbasis AI terus belajar dari pola lalu lintas, menyesuaikan kebijakan routing menggunakan wawasan profiling untuk meningkatkan penyeimbangan beban dinamis, prediksi kemacetan, dan manajemen lalu lintas jaringan cerdas [174].

Lebih lanjut, model ML seperti Artificial Neural Networks (ANN), Graph Neural Networks (GNN), dan Support Vector Machines (SVM) telah digunakan untuk menganalisis pola lalu lintas historis dan memprediksi lonjakan lalu lintas, memungkinkan alokasi sumber daya proaktif [175]. Selain itu, arsitektur deep learning seperti Residual Networks (ResNet) memungkinkan sistem berbasis AI memperkirakan okupansi tautan jaringan secara waktu nyata, meningkatkan keputusan routing dan efisiensi keseluruhan [176].

Keuntungan utama lain dari jaringan berbasis AI adalah toleransi kesalahan dan pemeliharaan prediktif. Model AI mendeteksi potensi kegagalan sebelum terjadi, sehingga meminimalkan waktu henti dan overhead operasional [177]. AI juga mengoptimalkan jaringan hemat energi menggunakan model reinforcement learning untuk memprediksi fluktuasi beban kerja dan menyesuaikan pemanfaatan server secara cerdas, yang mengarah pada konsumsi daya yang dioptimalkan [176]. Teknik-teknik ini mengandalkan Deteksi Anomali untuk terus memantau perilaku jaringan, mendeteksi degradasi kinerja, dan mengurangi ancaman keamanan.

Dengan mengintegrasikan AI/ML di berbagai aspek operasi jaringan, DCN modern bergeser dari kerangka kerja reaktif berbasis aturan ke sistem cerdas proaktif.

C. AI VS METODE TRADISIONAL DALAM DCN: PERBEDAAN UTAMA DAN TREN YANG MUNCUL

Teknik jaringan tradisional dalam DCN mengandalkan algoritme berbasis aturan, konfigurasi statis, dan penyesuaian reaktif, membuatnya stabil dan efisien secara komputasi, tetapi terbatas dalam hal adaptabilitas dan skalabilitas. Sebaliknya, pendekatan berbasis AI/ML memperkenalkan pengambilan keputusan dinamis, analitik prediktif, dan otomasi, memungkinkan jaringan mengantisipasi kemacetan, mengoptimalkan aliran lalu lintas, dan menyesuaikan sumber daya secara waktu nyata.

Metode tradisional sering memerlukan intervensi manual dan ambang yang telah ditetapkan, sedangkan model AI belajar terus-menerus dan dapat melakukan optimisasi proaktif tanpa input manusia. Dalam toleransi kesalahan, jaringan konvensional bergantung pada mekanisme redundansi dan failover yang meningkatkan biaya infrastruktur, sedangkan pemeliharaan prediktif berbasis AI mengidentifikasi kegagalan sebelum terjadi, mengurangi waktu henti. Demikian pula, dalam hal efisiensi energi, jaringan tradisional bergantung pada manajemen daya berbasis ambang tetap, yang sering menyebabkan inefisiensi sumber daya, sedangkan AI menyesuaikan konsumsi daya secara dinamis berdasarkan tuntutan beban kerja waktu nyata.

Meskipun AI memiliki keunggulan, ia memerlukan daya komputasi tinggi, dataset besar, dan optimisasi berkelanjutan, sehingga metode tradisional lebih dapat ditafsirkan, lebih ringan, dan lebih sederhana untuk diterapkan dalam lingkungan dengan sumber daya terbatas. Dengan kemajuan teknologi AI, pendekatan hibrida yang mengombinasikan adaptabilitas AI dengan stabilitas metode tradisional diperkirakan akan membentuk masa depan DCN otonom yang dapat mengoptimalkan diri sendiri.

Diskusi RQ4
Bagaimana teknik AI/ML memanfaatkan konsep jaringan untuk mengatasi tantangan DCN, dan bagaimana perbandingannya dengan pendekatan tradisional?

AI/ML meningkatkan DCN dengan memanfaatkan konsep jaringan kunci—Representasi, Profiling, dan Deteksi Anomali—untuk memungkinkan adaptasi waktu nyata, optimisasi prediktif, dan otomasi. Representasi menyusun data jaringan untuk manajemen lalu lintas berbasis AI, kontrol kemacetan, dan optimisasi routing. Profiling membantu menganalisis pola lalu lintas, mengalokasikan sumber daya secara efisien, dan memprediksi kegagalan. Deteksi Anomali memperkuat toleransi kesalahan dan keamanan dengan mengidentifikasi penyimpangan serta mengurangi ancaman secara waktu nyata.

Berbeda dengan metode statis dan berbasis aturan, AI terus belajar dan menyesuaikan, mengoptimalkan kinerja secara dinamis. Meskipun AI meningkatkan skalabilitas dan efisiensi, ia memerlukan daya komputasi tinggi, sehingga metode tradisional lebih efisien dalam lingkungan yang terbatas sumber daya. Masa depan DCN akan mengintegrasikan model hibrida yang menyeimbangkan adaptabilitas AI dengan stabilitas metode tradisional untuk otomatisasi dan keandalan yang lebih baik.

VII. TANTANGAN DALAM MENERAPKAN AI/ML UNTUK OPTIMISASI DAN MANAJEMEN DCN

Implementasi solusi AI/ML mengikuti siklus hidup terstruktur yang terdiri dari tiga fase kunci: desain, pengembangan, dan penerapan [178]. Pada fase desain, sistem AI/ML dikonseptualisasikan, risiko dinilai, dan kebutuhan data diidentifikasi. Fase pengembangan berfokus pada pemilihan model, pelatihan, dan optimisasi untuk memastikan skalabilitas dan efisiensi. Akhirnya, fase penerapan melibatkan integrasi model AI/ML ke dalam lingkungan dunia nyata, di mana kinerja, latensi, dan batasan sumber daya harus dikelola.

Seperti dibahas sebelumnya, ada beberapa manfaat integrasi solusi AI/ML untuk optimisasi dan manajemen DCN; namun, tantangan utama muncul yang perlu diatasi. Tantangan-tantangan ini mencakup siklus hidup AI, termasuk keterbatasan akuisisi data, kekhawatiran keamanan dan privasi, adaptabilitas model, keterbatasan inferensi waktu nyata, dan inefisiensi alokasi sumber daya. Gambar 4 menggambarkan tantangan yang dihadapi di setiap fase siklus hidup. Subbagian berikut mengkategorikan tantangan-tantangan ini dalam siklus hidup AI, memberikan analisis terstruktur tentang hambatan pada optimisasi DCN berbasis AI.

A. TANTANGAN PADA FASE DESAIN

Fase desain integrasi AI/ML dalam DCN melibatkan konseptualisasi model, penilaian risiko, dan pendefinisian kebutuhan data. Tantangan kunci termasuk akses terbatas ke data pelatihan berkualitas tinggi, menjamin privasi dan keamanan, serta melindungi model dari serangan adversarial. Pada subbagian berikut, kami membahas tantangan-tantangan ini secara rinci.

1. TANTANGAN MENGAKUISISI DATA UNTUK MELATIH MODEL AI/ML

Model AI memerlukan dataset untuk dilatih, dan dataset berkualitas tinggi jarang ditemukan, terutama di domain terkait jaringan di mana pengumpulan data terkadang dibatasi oleh kekhawatiran privasi, kendala penyimpanan, dan pembatasan akses. Banyak dataset bersifat proprietari atau memerlukan banyak izin untuk diakses, yang menyulitkan peneliti memperoleh data yang beragam dan representatif untuk melatih model AI. Hal ini terlihat dalam Gambar 5 yang menggambarkan jumlah dataset yang dipublikasikan setiap tahun. Dataset dunia nyata membawa beberapa tantangan, termasuk ketersediaan data, kompleksitas, dan kebutuhan pra-pemrosesan. Beberapa dataset, seperti dataset InSDN, mengumpulkan pengaturan jaringan spesifik, sehingga membatasi penerapan yang lebih umum [179]. Dataset berskala besar memerlukan sumber daya komputasi signifikan untuk pelatihan [180]. Kekhawatiran yang meningkat adalah privasi, yang lebih lanjut membatasi akses ke data jaringan sensitif, sehingga mempersulit berbagi dataset dan reproduksibilitas model [181]. Meskipun berharga untuk penelitian keamanan siber, dataset deteksi insiden sering kali menderita bias dan ketidaklengkapan [182]. Selain itu, jejak lalu lintas jaringan dunia nyata memerlukan pra-pemrosesan signifikan untuk mengelola kebisingan dan inkonsistensi [183].

Dataset sintetis menyediakan pengganti tetapi memiliki keterbatasan alami. Banyak bergantung pada asumsi mengenai model lalu lintas yang mungkin tidak sepenuhnya mencerminkan perilaku nyata [184]. Dataset simulasi seperti yang berbasis distribusi statistik dapat merepresentasikan pola lalu lintas nyata secara tidak akurat [185]. Demikian pula, dataset latensi dan kemacetan seringkali mengasumsikan kondisi jaringan ideal, sehingga mengabaikan variabel jaringan yang tidak terduga [186]. Meskipun data sintetis membantu mengatasi kekhawatiran privasi, efektivitasnya bergantung pada seberapa akurat ia meniru perilaku jaringan aktual [187].

Singkatnya, baik dataset sintetis maupun dunia nyata memiliki kesulitan yang mengganggu pelatihan model AI/ML. Mengatasi kendala-kendala ini memerlukan sistem berbagi data yang lebih baik, metode simulasi yang diperbarui, dan pendekatan hibrida yang menggabungkan data sintetis dan nyata untuk meningkatkan adaptabilitas model.

2. KEKHATIRAN KEAMANAN DAN PRIVASI DALAM MENERAPKAN MODEL BERBASIS AI DI DCN

Optimisasi jaringan berbasis AI bergantung pada jumlah besar data lalu lintas dan kinerja, yang sering dikumpulkan dari berbagai sumber dalam DCN. Menjamin kepatuhan terhadap regulasi privasi sambil mempertahankan kegunaan data adalah tantangan signifikan. Teknik seperti differential privacy dan federated learning dapat membantu mengurangi eksposur data sensitif tetapi memperkenalkan kompromi dalam akurasi model dan kecepatan konvergensi [188], [189]. Model ML yang digunakan dalam DCN rentan terhadap serangan adversarial, termasuk pencemaran data dan teknik pengelabuan model. Penyerang dapat memanipulasi data pelatihan atau masukan inferensi untuk merusak kinerja model, yang mengarah pada keputusan optimisasi jaringan yang salah. Menjamin pelatihan adversarial yang kuat dan mekanisme deteksi anomali penting untuk mengurangi ancaman keamanan ini [190], [191].

B. TANTANGAN PADA FASE PENGEMBANGAN

Fase pengembangan AI/ML dalam DCN berfokus pada pemilihan model, pelatihan, dan optimisasi untuk skalabilitas dan efisiensi. Tantangan utama meliputi keterbatasan inferensi waktu nyata, kebutuhan komputasi tinggi, dan adaptabilitas model terhadap kondisi jaringan dinamis. Solusi seperti kompresi model, pemrosesan edge, dan reinforcement learning membantu mengurangi masalah ini tetapi sering kali disertai kompromi dalam kinerja dan pemanfaatan sumber daya. Pada subbagian berikut, kami membahas tantangan-tantangan ini secara rinci.

1. PERTIMBANGAN KINERJA DAN LATENSI

Banyak teknik AI/ML memerlukan inferensi waktu nyata atau mendekati waktu nyata untuk membuat keputusan manajemen jaringan. Namun, model deep learning, khususnya yang digunakan dalam analitik prediktif, dapat memperkenalkan latensi inferensi yang signifikan. Tantangannya adalah menerapkan model AI yang ringan dan efisien yang mampu membuat keputusan cepat tanpa mengorbankan akurasi. Teknik seperti knowledge distillation dan quantization sedang dieksplorasi untuk mengurangi overhead inferensi sambil mempertahankan kinerja model [192], [193]. Model AI/ML memerlukan ingest data, pemrosesan, dan inferensi terus menerus, menambah overhead pada operasi DCN yang ada. Jalur pra-pemrosesan data harus dirancang dengan hati-hati untuk menghindari biaya komputasi berlebihan. Selain itu, kebutuhan pemrosesan AI terdistribusi di seluruh node jaringan memperkenalkan tantangan sinkronisasi, yang dapat memengaruhi kinerja keseluruhan strategi optimisasi berbasis AI [194], [195].

2. SKALABILITAS DAN ADAPTABILITAS MODEL AI/ML

Penerapan model AI/ML untuk optimisasi dan manajemen DCN menimbulkan kekhawatiran signifikan terkait skalabilitas dan adaptabilitas. Mengingat DCN adalah infrastruktur jaringan yang luas yang menghasilkan volume besar data telemetri jaringan, kemampuan model ini untuk memproses dan menganalisis dataset besar tersebut dalam skenario prediksi dunia nyata tetap sangat tidak pasti. Selain itu, pelatihan model ini memerlukan sumber daya komputasi yang considerable, dan dalam beberapa kasus, fase inferensi pun memberlakukan kebutuhan sumber daya yang signifikan. Hal ini memerlukan adopsi strategi seperti kompresi model dan teknik pemrosesan edge. Namun, pendekatan-pendekatan ini dapat mengompromikan kinerja keseluruhan model, sehingga menimbulkan trade-off kritis yang harus ditangani secara hati-hati [195], [196], [197].

DCN adalah lingkungan dinamis. Jaringan kompleks ini mengalami fluktuasi terus menerus dalam pola lalu lintas dan distribusi beban kerja. Model AI/ML harus beradaptasi secara dinamis terhadap perubahan tersebut, tetapi melatih ulang model secara waktu nyata menghadirkan tantangan dalam hal overhead komputasi dan waktu konvergensi. Pendekatan reinforcement learning dan pembelajaran online telah dieksplorasi untuk mengatasi masalah ini; namun, mencapai kinerja stabil sambil terus memperbarui model tetap menjadi tantangan kritis. Selain itu, kebutuhan pengumpulan data kontinu dan pra-pemrosesan untuk pembelajaran waktu nyata menambah overhead tambahan, yang memperumit penerapan dan manajemen sumber daya [194], [195], [198].

3. TANTANGAN EFISIENSI ENERGI

Integrasi model AI/ML untuk optimisasi DCN meningkatkan konsumsi daya keseluruhan, terutama selama fase pelatihan dan inferensi model. Solusi AI hemat energi harus menyeimbangkan akurasi dan biaya komputasi, memerlukan pendekatan baru seperti jaringan saraf ringan, akselerator perangkat keras, dan strategi manajemen daya adaptif. Penelitian masa depan tentang teknik AI hijau bertujuan meminimalkan jejak karbon manajemen DCN berbasis AI sambil mempertahankan efektivitas optimisasi [192], [199].

C. TANTANGAN PADA FASE PENERAPAN

Fase penerapan AI/ML dalam DCN melibatkan integrasi model ke dalam lingkungan dunia nyata, sambil mengelola kinerja, latensi, dan batasan sumber daya. Tantangan kunci termasuk alokasi sumber daya yang efisien, konsumsi daya tinggi, dan keadilan dalam distribusi beban kerja. Teknik seperti federated learning, pendekatan hibrida cloud-edge, dan manajemen daya adaptif bertujuan mengoptimalkan penerapan, tetapi menyeimbangkan skalabilitas dan efisiensi tetap menjadi tantangan. Pada subbagian berikut kami membahas tantangan-tantangan ini secara rinci.

1. TANTANGAN EFISIENSI ENERGI DALAM PENERAPAN

Penerapan model AI/ML dalam DCN secara signifikan memengaruhi konsumsi energi karena inferensi dan manajemen sumber daya yang terus menerus memerlukan daya komputasi besar. Tidak seperti fase pelatihan, di mana penggunaan energi terkonsentrasi dalam lonjakan, penerapan menuntut daya berkelanjutan untuk eksekusi model waktu nyata, pemrosesan data, dan optimisasi jaringan. Konsumsi daya tinggi selama inferensi dapat membebani infrastruktur yang ada, meningkatkan biaya operasional dan dampak lingkungan. Untuk mengatasi tantangan ini, jaringan saraf ringan, akselerator perangkat keras, dan strategi manajemen daya adaptif telah diusulkan. Federated learning dan pendekatan hibrida cloud-edge membantu mendistribusikan beban kerja secara efisien, mengurangi beban pada DC terpusat. Namun, mengoptimalkan penerapan AI untuk efisiensi energi tanpa mengorbankan kinerja tetap menjadi tantangan kritis yang memerlukan kemajuan lebih lanjut dalam teknik AI hijau dan mekanisme penjadwalan sadar daya.

2. TANTANGAN ALOKASI DAN PEMANFAATAN SUMBER DAYA

Model AI/ML telah dimanfaatkan untuk mengoptimalkan alokasi sumber daya dalam DCN dengan memprediksi kemacetan jaringan, menyeimbangkan beban kerja, dan meningkatkan penjadwalan tugas. Namun, menerapkan strategi alokasi sumber daya berbasis ML memerlukan data granular tingkat tinggi, inferensi waktu nyata, dan loop umpan balik yang kuat untuk menghindari degradasi kinerja.

Selain itu, model ML harus menjamin keadilan dalam alokasi sumber daya, mencegah bias dalam distribusi tugas, dan menghindari kontensi sumber daya yang dapat menyebabkan kemacetan [198], [200], [201]. Meskipun model AI/ML bertujuan mengoptimalkan kinerja jaringan, ia memperkenalkan tantangan konsumsi sumber daya. Pelatihan dan penerapan model AI skala besar memerlukan sumber daya komputasi signifikan, sering kali menyebabkan perangkat keras kurang dimanfaatkan selama fase pelatihan non-puncak. Implementasi strategi konsolidasi beban kerja berbasis AI, seperti federated learning atau pendekatan hibrida cloud-edge, dapat mengurangi inefisiensi. Namun, menjamin penerapan model AI yang efisien tanpa meningkatkan konsumsi daya atau membebani infrastruktur jaringan yang ada tetap menjadi perhatian [191], [192], [201].

Diskusi RQ5
Apa saja tantangan utama dalam merancang, mengembangkan, dan menerapkan solusi berbasis AI/ML untuk optimisasi dan manajemen DCN?

Tantangan utama dalam penelitian DCN dapat dikategorikan ke dalam tiga area kunci:

- Tantangan Desain:
  - Kekurangan data, kekhawatiran privasi, dan risiko adversarial.
- Tantangan Pengembangan:
  - Keterbatasan inferensi waktu nyata, tuntutan komputasi tinggi, dan adaptabilitas model. Solusi seperti kompresi model dan pemrosesan edge membantu tetapi memperkenalkan trade-off.
- Tantangan Penerapan:
  - Alokasi sumber daya, konsumsi energi, dan kekhawatiran keadilan diatasi melalui federated learning dan strategi cloud-edge.

Meskipun ada kemajuan, memastikan solusi DCN berbasis AI yang efisien dan skalabel memerlukan eksplorasi lebih lanjut tentang optimisasi, keamanan, dan strategi penerapan yang berkelanjutan.

IX. DISKUSI

Penelitian tentang DCN telah berkembang secara bertahap selama sepuluh tahun terakhir, menggambarkan peningkatan signifikan dalam studi tentang optimisasi dan manajemen DCN. Namun, DCN tetap kurang diteliti dibandingkan bidang penelitian DC lainnya. Perbedaan ini menekankan pentingnya memberi perhatian lebih pada DCN untuk memastikan bahwa mereka berubah sejalan dengan perkembangan teknologi DC kritis lainnya, sistem penyimpanan, dan komputasi awan. Meskipun laju penelitian lebih lambat, para peneliti telah mencapai kemajuan signifikan dalam menangani isu efisiensi jaringan, pengurangan latensi, peningkatan penyeimbangan beban, dan penguatan ketahanan sistem secara keseluruhan.

Meliputi kontrol kemacetan, rekayasa lalu lintas, penyeimbangan beban, SDN, dan toleransi kesalahan, tinjauan skoping ini menguraikan tema utama penelitian DCN. Topik-topik ini menunjukkan berbagai peluang dan tantangan di bidang ini, serta upaya kolektif untuk meningkatkan struktur dan operasi DCN. Studi ini juga mengeksplorasi bagaimana AI dan ML mengubah manajemen jaringan untuk memberikan otomatisasi cerdas, optimisasi aliran lalu lintas, prediksi kegagalan sistem, dan optimisasi aliran lalu lintas. Selain itu, sistem keamanan berbasis AI dan ML semakin membantu mendeteksi dan mengurangi ancaman siber, sehingga meningkatkan ketahanan DCN modern.

Untuk menjawab pertanyaan penelitian inti yang diusulkan, tinjauan ini menyoroti kemajuan utama dalam optimisasi DCN. Kontrol kemacetan berbasis AI, strategi lalu lintas berbasis SDN, dan penyeimbangan beban adaptif adalah beberapa solusi yang sedang aktif dieksplorasi untuk meningkatkan efisiensi. Selain itu, penerapan AI dan ML yang muncul dalam pemeliharaan prediktif dan manajemen sumber daya hemat energi menekankan pentingnya otomasi dalam DCN. Arsitektur hibrida yang mengintegrasikan teknologi optik dan nirkabel telah dikembangkan, menghasilkan transmisi data lebih cepat dan latensi lebih rendah. Dengan menggabungkan inovasi-inovasi ini, tinjauan ini memberikan perspektif holistik tentang transformasi DCN sebagai respons terhadap meningkatnya tuntutan komputasi dan jaringan.

Aspek penting lain dari penelitian DCN berputar di sekitar pemodelan dan representasi, profiling, serta deteksi anomali, yang berfungsi sebagai prinsip jaringan fundamental untuk meningkatkan efisiensi dan keamanan. Pemodelan dan representasi menyediakan kerangka terstruktur untuk menganalisis lalu lintas jaringan dan mengoptimalkan routing, sehingga memungkinkan arsitektur yang lebih adaptif dan skalabel. Teknik profiling memungkinkan pemahaman yang lebih dalam tentang pola lalu lintas, perilaku jaringan, dan pemanfaatan sumber daya, yang pada gilirannya membantu alokasi beban kerja dinamis dan manajemen kemacetan yang lebih baik. Deteksi anomali memainkan peran penting dalam memastikan ketahanan jaringan dengan mengidentifikasi ancaman keamanan, hambatan kinerja, dan titik kegagalan sebelum mereka menyebabkan gangguan. Penerapan teknik-teknik ini secara holistik dapat membantu mengatasi banyak tantangan DCN yang ada, membuka jalan bagi infrastruktur jaringan yang lebih tangguh, cerdas, dan mampu mengoptimalkan diri.

Dengan menjawab RQ1-RQ5, studi kami menunjukkan bahwa (1) profiling berbasis telemetri (RQ1) memberikan basis yang andal untuk perilaku jaringan normal; (2) model peramalan sadar fitur (RQ2) secara signifikan meningkatkan akurasi prediksi jangka pendek; (3) deteksi anomali berbasis graf (RQ3) secara efektif mengintegrasikan data struktural dan temporal untuk mengurangi false positive; (4) diagnosis kausal melalui graf kejadian (RQ4) menawarkan wawasan yang dapat ditafsirkan tentang asal anomali; dan (5) kerangka kerja yang diusulkan memiliki skalabilitas dan modularitas (RQ5) yang mendukung penerapan mulus di lingkungan pusat data berskala besar. Secara kolektif, temuan-temuan ini mengonfirmasi efektivitas pendekatan multistage berbasis AI untuk pemantauan DCN proaktif dan membuka jalan bagi peningkatan manajemen jaringan waktu nyata di masa depan.

Salah satu kontribusi kunci tinjauan ini adalah analisis terstruktur penelitian DCN di berbagai tema, memberikan pandangan menyeluruh tentang kemajuan saat ini dan area yang masih memerlukan perhatian. Metodologi tinjauan skoping, yang dipandu oleh PRISMA-ScR, memastikan pemeriksaan yang teliti dan metodologis terhadap penelitian yang ada. Selain itu, pengenalan pendekatan penyaringan studi berbasis LLM dan pemodelan topik menunjukkan bagaimana otomasi dapat meningkatkan tinjauan literatur dalam area penelitian berskala besar, sambil melayani peneliti dan praktisi. Diskusi mengenai integrasi AI dan ML dalam DCN lebih lanjut memperdalam pemahaman tentang keuntungan dan tantangan menerapkan solusi berbasis AI pada skala besar.

Tinjauan ini berkontribusi pada penelitian DCN dengan menyediakan sintesis terstruktur tentang tema utama, tantangan, dan tren yang muncul di seluruh bidang. Dengan mengidentifikasi celah di area seperti deteksi anomali waktu nyata, kontrol lalu lintas adaptif, dan manajemen jaringan hemat energi, tinjauan ini menyoroti arah penelitian yang dapat ditindaklanjuti untuk mengoptimalkan kinerja DCN. Selain itu, metodologi skoping yang diadopsi menunjukkan bagaimana otomasi dapat meningkatkan pemetaan literatur berskala besar, mendukung kemajuan desain dan operasi DCN yang lebih sistematis dan berinformasi.

X. TREN MASA DEPAN DALAM PENELITIAN DCN

Evolusi DCN dibentuk oleh meningkatnya tuntutan akan otomasi, kecerdasan edge, keberlanjutan, dan keamanan. Ketika pusat data semakin mendukung layanan cloud-native, berbasis AI, dan sensitif latensi, beberapa jalur penelitian yang menjanjikan telah muncul.

Integrasi AI dalam Radio Access Networks (AI-RAN) dan Multi-access Edge Computing (AI-MEC) akan merevolusi efisiensi dan responsivitas jaringan. AI-RAN secara efektif memanfaatkan algoritme pembelajaran mesin untuk mengoptimalkan alokasi sumber daya dan meningkatkan pengalaman pengguna dengan memprediksi pola lalu lintas serta menyesuaikan parameter jaringan secara dinamis [202]. Meskipun AI-MEC juga menggunakan kemampuan edge computing untuk memproses data lebih dekat ke sumber, sehingga mengurangi latensi dan meningkatkan efisiensi operasional, dampak spesifiknya pada aplikasi waktu nyata harus dieksplorasi melalui penelitian lebih lanjut [203].

Konsep dark network operation centers (DNOC), yang dicirikan oleh intervensi manusia minimal hingga nihil dalam manajemen dan operasi data, menjadi tren penting dalam evolusi pusat data. Transformasi ini terutama didorong oleh kebutuhan yang meningkat akan efisiensi operasional dan keterjangkauan energi dalam konteks komputasi awan dan infrastruktur digital yang luas. Integrasi teknologi otomasi canggih memainkan peran penting dalam pergeseran ini, memungkinkan pemantauan otonom dan kontrol operasi pusat data. Misalnya, platform edge computing baru memfasilitasi pemantauan operasional cerdas menggunakan sensor nirkabel dan terpasang, yang mengoptimalkan distribusi beban kerja, sehingga meningkatkan efisiensi energi dan keandalan operasional [204]. Selain itu, arsitektur inovatif yang memanfaatkan konverter DC-DC dua arah penting untuk memastikan keselamatan dan stabilitas dalam sistem pasokan daya di DNOC, terutama mengingat tuntutan operasional yang berkembang untuk manajemen daya di pusat data geo-terdistribusi yang mendukung layanan cloud global [205], [206]. Unsur penting lain yang memengaruhi tren ini adalah penelitian berkelanjutan tentang strategi manajemen sumber daya yang bertujuan meminimalkan biaya dan meningkatkan kinerja di berbagai lingkungan operasional [207]. Munculnya sistem otonom di pusat data menandakan kemajuan teknologi yang lebih luas, di mana pengawasan manusia yang berkurang dapat mengoptimalkan efisiensi dan mengurangi kesalahan operasional sekaligus meningkatkan skalabilitas. Pergeseran ini menuju infrastruktur teknologi yang lebih berkelanjutan dan efisien penting untuk mengelola beban kerja dan tuntutan energi yang meningkat [208], [209].

Keberlanjutan telah menjadi fokus utama untuk penelitian DCN di masa depan, dengan upaya signifikan diarahkan pada pengurangan jejak karbon dan peningkatan efisiensi energi. Strategi seperti transisi ke sumber energi terbarukan, optimisasi sistem pendinginan, dan penerapan praktik ekonomi sirkular penting untuk meminimalkan dampak lingkungan [210], [211]. Studi menunjukkan bahwa penghematan energi substansial dapat dicapai melalui praktik manajemen inovatif, termasuk strategi konservasi energi dan teknik alokasi sumber daya berbasis AI [212], [213], [214].

Integrasi komputasi kuantum ke dalam kerangka kerja keamanan pusat data menghadirkan peluang tak tertandingi untuk meningkatkan strategi perlindungan data. Kriptografi kuantum dapat menawarkan tingkat keamanan yang jauh lebih tinggi daripada metode klasik dengan memungkinkan saluran komunikasi aman yang secara teoretis kebal terhadap penyadapan [215]. Karena pusat data menyimpan jumlah besar informasi sensitif, penerapan langkah-langkah keamanan canggih ini akan menjadi semakin penting untuk melindungi terhadap ancaman siber yang terus berkembang [216].

Lanskap DCN berkembang dengan cepat, didorong oleh kemajuan dalam AI, imperatif keberlanjutan, protokol keamanan yang ditingkatkan, dan fokus pada infrastruktur yang dapat diprogram. Seiring tren-tren ini berkembang, penelitian akan memainkan peran kritis dalam mengembangkan operasi pusat data yang lebih efisien, tangguh, dan aman untuk memenuhi tuntutan masa depan yang didorong data. Dengan komitmen berkelanjutan terhadap pendekatan inovatif, industri pusat data dapat mengaspirasikan kerangka kerja yang lebih berkelanjutan dan cerdas.

XI. KESIMPULAN

Dalam tinjauan skoping ini, kami memetakan kumpulan penelitian yang ada dan mensintesis tema-tema, metode, dan tantangan yang berlaku di seluruh domain DCN. Tujuan kami adalah menyediakan tinjauan terstruktur yang menyoroti tren utama dan mengidentifikasi area di mana penyelidikan lebih lanjut yang spesifik teknologi dapat mendorong kemajuan bermakna. Beberapa arah penelitian menarik sedang dieksplorasi. Upaya masa depan harus fokus pada integrasi mulus solusi AI dan ML dengan operasi jaringan waktu nyata untuk meningkatkan adaptabilitas dan kemampuan prediktif. Kerangka benchmarking yang lebih komprehensif diperlukan untuk mengevaluasi solusi jaringan berbasis AI relatif terhadap metode tradisional. Selain itu, keberlanjutan tetap menjadi aspek krusial, dan penelitian tentang desain DCN hemat energi penting untuk mengurangi jejak lingkungan pusat data berskala besar. Area menjanjikan lainnya termasuk jaringan kuantum dan blockchain, yang dapat menyediakan keamanan yang ditingkatkan dan manajemen jaringan terdesentralisasi. Saat DCN terus berkembang, kolaborasi antar-disiplin antara jaringan, ML, dan komputasi awan akan membentuk arsitektur generasi berikutnya. Adopsi edge computing dan 5G yang terus meningkat menghadirkan peluang menarik untuk mengoptimalkan aliran data dan meminimalkan latensi dalam lingkungan terdistribusi. Akhirnya, solusi berbasis AI kemungkinan besar akan menjadi landasan optimisasi DCN masa depan, memungkinkan jaringan beroperasi dengan efisiensi, kecerdasan, dan ketahanan yang lebih besar.

Akhirnya, tinjauan ini menyajikan kajian komprehensif tentang penelitian DCN, menerangi inovasi utama, tantangan, dan kemungkinan masa depan. Dengan mengatasi celah dalam literatur yang ada dan mengidentifikasi peluang untuk studi lebih lanjut, studi ini berkontribusi pada upaya yang lebih luas untuk meningkatkan kinerja, skalabilitas, dan keberlanjutan DCN. Seiring kemajuan teknologi mempercepat, penelitian dan kolaborasi berkelanjutan akan menjadi kunci dalam merumuskan metodologi saat ini dan mendorong gelombang terobosan berikutnya dalam optimisasi DCN. Masa depan DCN menjanjikan, dan dengan AI terus memimpin, jaringan ini akan menjadi lebih otonom, adaptif, dan tak tergantikan untuk mendukung lanskap digital yang terus berkembang.

APENDIKS

DAFTAR SINGKATAN
Singkatan Istilah Penuh

AI Kecerdasan Buatan
API Application Programming Interface
BGP Border Gateway Protocol
CPU Central Processing Unit
DCN Data Center Network
DNS Domain Name System
FPGA Field-Programmable Gate Array
GPU Graphics Processing Unit
HTTP Hypertext Transfer Protocol
HTTPS Hypertext Transfer Protocol Secure
IoT Internet of Things
LAN Local Area Network
ML Pembelajaran Mesin
MPLS Multiprotocol Label Switching
NFV Network Function Virtualization
NIC Network Interface Card
OSPF Open Shortest Path First
PUE Power Usage Effectiveness
QoS Quality of Service
RTT Round-Trip Time
SDN Software-Defined Networking
SLA Service Level Agreement
SSD Solid State Drive
TCO Total Cost of Ownership
TCP Transmission Control Protocol
VLAN Virtual Local Area Network
VM Virtual Machine
WAN Wide Area Network

PENGHARGAAN
(Kogul Srikandabala dan Kirishnni Prabagar berkontribusi secara setara terhadap karya ini.)

REFERENSI

[1] C. Wo dan R. Buyya, Cloud Data Centers and Cost Modeling. San Mateo, CA, USA: Morgan Kaufmann, Mar. 2015

[2] W. Xia, P. Zhao, Y. Wen, dan H. Xie, “A survey on data center networking (DCN): Infrastructure and operations,” IEEE Commun. Surveys Tuts., vol. 19, no. 1, pp. 640-656, Ist Quart., 2017.

[3] R.R. Schaller, “Moore's law: Past, present and future,” IEEE Spectrum, vol. 34, no. 6, pp. 52-59, Jun. 1997.

[4] R. McGeer, P. Mahadevan, dan S. Banerjee, “On the complexity of power minimization schemes in data center networks,” in Proc. IEEE Global Telecommun. Conf. GLOBECOM, Dec. 2010, pp. 1-5.

[5] L. Popa, S. Ratnasamy, G. Iannaccone, A. Krishnamurthy, dan I. Stoica, “A cost comparison of datacenter network architectures,” in Proc. 6th Int. Conf., Nov. 2010, pp. 1-12.

[6] C. E. Rothenberg, “Re-architected cloud data center networks and their impact on the future Internet,” in New Network Architectures. Cham, Switzerland: Springer, 2010, pp. 179-187.

[7] L. Schares, D. M. Kuchta, dan A. F. Benner, “Optics in future data center networks,” in Proc. 18th IEEE Symp. High Perform. Interconnec, Aug. 2010, pp. 104-108.

[8] Y. Shang, D. Li, dan M. Xu, “A comparison study of energy proportionality of data center network architectures,” in Proc. 32nd Int. Conf. Distrib. Comput. Syst. Workshops, Jun. 2012, pp. 1-7.

[9] K. Wu, J. Xiao, dan L. M. Ni, “Rethinking the architecture design of data center networks,” Frontiers Comput. Sci., vol. 6, no. 5, pp. 596-603, Sep. 2012.

[10] R. P. Tahiliani, M. P. Tahiliani, dan K. C. Sekaran, “TCP variants for data center networks: A comparative study,” in Proc. Int. Symp. Cloud Services Comput., Dec. 2012, pp. 57-62.

[11] C. Kachris dan I. Tomkos, “The rise of optical interconnect networks,” in Proc. 14th Int. Conf. Transparent Opt. Netw., Jul. 2012, pp. 1-4.

[12] L. Xu, A. Singh, dan Y. Zhan, “Optically interconnected data center networks,” in Proc. Opt. Fiber Commun. Conf, 2012, pp. 1-3.

[13] X.L. Wei, M. Chen, J.-H. Fan, G.-M. Zhang, dan Z.-Y. Lu, “Architecture of the data center network: Architecture of the data center network,” J. Softw., vol. 24, no. 2, pp. 295-316, Dec. 2013.

[14] N. Farrington dan A. Andreyev, “Facebook's data center network architecture,” in Proc. Opt. Interconnects Conf., May 2013, pp. 49-50.

[15] J. Zhang, F. Ren, dan C. Lin, “Survey on transport control in data center networks,” IEEE Netw., vol. 27, no. 4, pp. 22-26, Jul. 2013.

[16] J. Perelló et al., “All-optical packet/circuit switching-based data center network for enhanced scalability, latency, and throughput,” IEEE Netw., vol. 27, no. 6, pp. 14-22, Nov. 2013.

[17] C. Kachris dan I. Tomkos, “Power consumption evaluation of all-optical data center networks,” Cluster Comput., vol. 16, no. 3, pp. 611-623, Aug. 2012.

[18] K. Bilal, S. U. Khan, dan A. Y. Zomaya, “Green data center networks: Challenges and opportunities,” in Proc. 11th Int. Conf. Frontiers Inf. Technol., Dec. 2013, pp. 229-234.

[19] P.P. Jiang, C.Q. Yu, dan Y. H. Peng, “Energy-saving in optical data center networks,” Appl. Mech. Mater., vols. 411-414, pp. 634-637, Sep. 2013.

[20] M. F. Bari, R. Boutaba, R. Esteves, L. Z. Granville, M. Podlesny, M. G. Rabbani, Q. Zhang, dan M. F. Zhani, “Data center network virtualization: A survey,” IEEE Commun. Surveys Tuts., vol. 15, no. 2, pp. 909-928, 2nd Quart., 2013.

[21] Y. Cai, Y. Yan, Z. Zhang, dan Y. Yang, “Survey on converged data center networks with DCB and FCoE: Standards and protocols.” IEEE Netw., vol. 27, no. 4, pp. 27-32, Jul. 2013.

[22] A. Hendel, “Large-scale data center networks,” in Proc. Commun. Conf., 2014, pp. Th4J.1- Th4J.1.

[23] F. Yao, J. Wu, G. Venkataramani, dan S. Subramaniam, “A comparative analysis of data center network architectures,” in Proc. IEEE Int. Conf. Commun. (ICC), Jun. 2014, pp. 3106-3111.

[24] Y. Ren, Y. Zhao, P. Liu, K. Dou, dan J. Li, “A survey on TCP incast in data center networks,” Int. J. Commun. Syst., vol. 27, no. 8, pp. 1160-1172, Jul. 2012.

[25] H. X. Wu, X. L. Yang, dan M. Zhang, “Optically interconnected data center networks: A survey and new perspectives,” in Proc. Opt. Fiber Commun. Conf., vols. 462-463, pp. 1028-1035, Nov. 2013.

[26] K. Kitayama, Y.-C. Huang, Y. Yoshida, R. Takahashi, dan M. Hayashitani, “Optical packet and path switching intra-data center network: Enabling technologies and network performance with intelligent flow control,” in Proc. Eur. Conf. Opt. Commun. (ECOC), Sep. 2014, pp. 1-3.

[27] M. Fayyaz dan K. Aziz, “Classification of optical interconnects in data center networks,” in Proc. 12th Int. Conf. Frontiers Inf. Technol., Dec. 2014, pp. 61-66.

[28] N. Calabretta, W. Miao, S. D. Lucente, J. Luo, dan H. J. S. Dorren, “Scalable and low latency optical packet switching architectures for high performance data center networks,” in Adv. Photon. Commun., 2014.

[29] K. Kitayama, Y. Huang, Y. Yoshida, R. Takahashi, dan M. Hayashitani, “OPS/OCS intra-data center network with intelligent flow control,” in Adv. Photon. Commun., 2014.

[30] H. Qi, M. Shiraz, J.-Y. Liu, A. Gani, Z. A. Rahman, dan T. A. Altameem, “Data center network architecture in cloud computing: Review, taxonomy, and open research issues,” J. Zhejiang Univ. Sci. C, vol. 15, no. 9, pp. 776-793, Sep. 2014.

[31] A. Hammadi dan L. Mhamdi, “A survey on architectures and energy efficiency in data center networks,” Comput. Commun., vol. 40, pp. 1-21, Mar. 2014.

[32] K. Bilal, S. U. R. Malik, O. Khalid, A. Hameed, E. Alvarez, V. Wijaysekara, R. Irfan, S. Shrestha, D. Dwivedy, M. Ali, U. S. Khan, A. Abbas, N. Jalil, dan S. U. Khan, “A taxonomy and survey on green data center networks.” Future Gener. Comput. Syst., vol. 36, pp. 189-208, Jul. 2014.

[33] B. Maggs, “A universal approach to data center network design,” in Proc. 26th ACM Symp. Parallelism Algorithms Archit., Jun. 2014, p. 246.

[34] A. Lonare dan V. Gulhane, “Addressing agility and load balance in fat-tree data center network—A review,” in Proc. 2nd Int. Conf. Electron. Commun. Syst. (ICECS), Feb. 2015, pp. 965-971.

[35] M. Fayyaz, K. Aziz, dan G. Mujtaba, “Blocking probability in optical interconnects in data center networks,” Photonic Netw. Commun., vol. 30, no. 2, pp. 204-222, May 2015.

[36] W. Hou, L. Guo, Y. Liu, C. Yu, dan Y. Zong, “Resource management and control in converged optical data center networks: Survey and enabling technologies,” Comput. Netw., vol. 88, pp. 121-135, Sep. 2015.

[37] R. Takahashi, T. Segawa, S. Ibrahim, T. Nakahara, H. Ishikawa, A. Hiramatsu, Y.-C. Huang, dan K.-i. Kitayama, “Torus data center network with smart flow control enabled by hybrid optoelectronic routers [Invited],” J. Opt. Commun. Netw., vol. 7, no. 12, pp. B141-B152, Dec. 2015.

[38] C. Kachris dan I. Tomkos, “A roadmap on optical interconnects in data centre networks,” in Proc. 17th Int. Conf. Transparent Opt. Netw. (ICTON), Jul. 2015, pp. 1-3.

[39] K.-I. Kitayama, Y.-C. Huang, Y. Yoshida, R. Takahashi, T. Segawa, S. Ibrahim, T. Nakahara, Y. Suzaki, M. Hayashitani, Y. Hasegawa, Y. Mizukoshi, dan A. Hiramatsu, “Torus-topology data center network based on optical packet/agile circuit switching with intelligent flow management,” J. Lightw. Technol., vol. 33, no. 5, pp. 1063-1071, Mar. 2015.

[40] R. Rojas-Cessa, Y. Kaymak, dan Z. Dong, “Schemes for fast transmission of flows in data center networks,” IEEE Commun. Surveys Tuts., vol. 17, ...
