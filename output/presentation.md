# Presentation Slides: Optimisasi dan Manajemen Jaringan Pusat Data (DCN)

## Slide 1: Judul & Hook
*   **Topik Utama:** Optimisasi dan Manajemen Jaringan Pusat Data (DCN) melalui Pendekatan Kecerdasan Buatan (AI) dan Pembelajaran Mesin (ML).
*   **Lonjakan Trafik Data:** Era *streaming*, *e-commerce*, komputasi awan, dan layanan AI menciptakan beban jaringan yang eksponensial secara global.
*   **Perkembangan Jomplang:** Kemampuan komputasi prosesor *server* meningkat pesat (sesuai Hukum Moore), namun arsitektur jaringan tertinggal jauh di belakang.
*   **Ancaman *Bottleneck*:** Infrastruktur konvensional berisiko tinggi mengalami latensi, kemacetan data, dan inefisiensi konsumsi energi.
*   **Solusi Pintar:** Transformasi menuju analitik prediktif dan manajemen otonom menggunakan AI/ML mulai menggeser paradigma lama.

## Slide 2: Latar Belakang & Masalah (Research Gap)
*   **Keterbatasan Metode Tradisional:** Sangat bergantung pada konfigurasi statis, algoritma *rule-based*, dan penyesuaian reaktif sehingga lambat dalam beradaptasi pada fluktuasi lalu lintas dinamis.
*   **Kompleksitas DCN Modern:** Skala fasilitas DCN yang masif gagal ditangani oleh pendekatan jaringan konvensional.
*   **Minimnya *Framework* Menyeluruh:** Belum adanya solusi sistem AI terintegrasi secara *end-to-end* yang benar-benar siap diterpakan di industri nyata.
*   **Tuntutan Energi Global:** DC mengonsumsi daya listrik yang sangat tinggi, sehingga menuntut optimisasi ekstra demi keberlanjutan (*Green Computing*).
*   **Celah Riset Literatur:** Kajian sebelumnya cenderung fokus pada aspek terisolasi (misal, hanya soal routing saja atau energi saja) dan jarang menganalisis penerapan AI/ML secara sistematis.

## Slide 3: Metodologi Penelitian
*   **Desain Studi:** Sebuah *scoping review* komprehensif yang berbasis pada protokol terstandar PRISMA-ScR.
*   **Penyaringan Otomatis:** Memanfaatkan pendekatan hibrida (integrasi skrip API CrossRef dan *Large Language Models*/LLM) untuk menangani klasifikasi tematik volume dokumen yang masif (1.864 literatur awal) secara efisien.
*   **Filter Ketat:** Menyaring dokumen ganda, memeriksa tipe akses (*open access*, bahasa Inggris), hingga memvalidasi kelayakan topik yang fokus utamanya adalah DCN.
*   **Hasil Ekstraksi Akhir:** Diperoleh 1.636 studi valid yang akhirnya dikelompokkan secara terstruktur ke dalam 7 domain riset kunci.

## Slide 4: 7 Tema Penelitian Utama DCN
Penelitian ini memetakan 7 domain terpenting dalam optimisasi DCN:
1.  **Jaringan Optik (20%):** Transmisi data berkecepatan ultra-tinggi dengan latensi minimum dan konsumsi daya lebih rendah.
2.  **Manajemen Sumber Daya & Efisiensi Energi (18%):** Optimisasi operasional *cloud* untuk memangkas emisi dan konsumsi listrik.
3.  **Toleransi Kesalahan & Ketahanan (15%):** Meningkatkan keandalan operasional, pemeliharaan prediktif, dan pemulihan gangguan dari *error*.
4.  **Kontrol Kemacetan (14%):** Pencegahan hambatan trafik dan *packet loss* di kondisi dinamis.
5.  **Penjadwalan Aliran (13%):** Jaringan yang sadar-tenggat waktu (*deadline-aware*) untuk aplikasi yang sangat sensitif pada latensi.
6.  **Software-Defined Networking / SDN (12%):** Pemisahan *control plane* dan *data plane* untuk kontrol trafik sentral yang dinamis.
7.  **Penyeimbangan Beban (8%):** Distribusi lalu lintas yang merata agar tidak terjadi kelebihan/kekurangan utilisasi beban sistem.

## Slide 5: Konsep Jaringan Inti dalam DCN
Inovasi DCN didukung oleh tiga pilar jaringan secara fundamental:
*   **Representasi:** Pemodelan struktur jaringan, lalu lintas data, dan perilaku *routing* sebagai dasar dalam analisis cerdas berbasis AI.
*   **Profiling:** Menganalisis secara spesifik pola lalu lintas jaringan, penggunaan sumber daya, dan *bandwidth* guna menciptakan sistem adaptasi seketika (*real-time*).
*   **Deteksi Anomali:** Identifikasi sigap terhadap serangan keamanan (seperti manipulasi DDoS), salah konfigurasi, serta tanda-tanda gagal sistem sebelum stabilitas berdampak serius.
*   *Sinergi Ketiganya:* Representasi memberikan struktur ruang lingkup jaringan, Profiling mengekstrak wawasan dinamis, dan Deteksi Anomali memurnikan aliran dari ketidaknormalan.

## Slide 6: Analisis Perbandingan Tradisional vs AI/ML
*   **Pendekatan Tradisional (84% Riset):**
    *   Sifatnya berbasis aturan, bergantung pada ambang batas statis, dan reaktif (bertindak setelah kejadian).
    *   *Kelebihan:* Sangat stabil, lebih mudah ditafsirkan, dan hemat biaya komputasi.
    *   *Kelemahan:* Kaku, lambat beradaptasi pada beban *real-time*, dan bergantung pada mekanisme redundansi kabel yang mahal.
*   **Pendekatan AI/ML (16% Riset):**
    *   Sifatnya adaptif, analitik prediktif, dan berorientasi otonom.
    *   *Kelebihan:* Mampu mencegah *error* sebelum terjadi (*predictive maintenance*), pengaturan trafik cerdas, dan mitigasi kemacetan proaktif.
    *   *Kelemahan:* Membutuhkan beban inferensi/komputasi yang tinggi, rentan dimanipulasi data (*data poisoning*), dan krisis data *training* asli.

## Slide 7: Tantangan AI - Fase Desain
*   **Kelangkaan Dataset Berkualitas:** Implementasi model ML amat butuh dataset lalu lintas DCN riil yang berkualitas, namun data ini sangat dijaga ketat oleh masalah privasi industri. Dataset sintetis sering kali gagal mempresentasikan kondisi jaringan yang sebenarnya.
*   **Keamanan & Privasi:** Memastikan kerahasiaan data *Data Center* saat fase *training* adalah sebuah kewajiban. Solusi privasi dapat berdampak pada penalti kecepatan *training*.
*   **Ancaman *Adversarial Attacks*:** Algoritma model ML bisa "ditipu" (mis. melalui serangan injeksi data palsu) agar sistem AI mengambil langkah manajemen jaringan yang destruktif.

## Slide 8: Tantangan AI - Fase Pengembangan
*   **Latensi & Komputasi Inferensi:** Karena AI harus mengambil langkah *real-time*, menuntut proses komputasi yang kilat. Solusi model yang lambat justru menaikkan latensi, mengalahkan tujuannya sendiri.
*   **Skalabilitas Model:** Lingkungan DCN super-kompleks menuntut AI untuk terus menyesuaikan pola *traffic* yang fluktuatif setiap detik. Melatih ulang model secara terus menerus amat memberatkan perangkat keras.
*   **Trade-off Optimalisasi:** Metode kompresi model AI atau pengolahan di sisi *edge* membantu mengurangi beban, tetapi terkadang mengorbankan tingkat akurasi pemecahan masalah model tersebut.

## Slide 9: Tantangan AI - Fase Penerapan (Deployment)
*   **Paradoks Efisiensi Energi:** Secara ironis, AI diusulkan untuk menghemat daya DCN, padahal di saat bersamaan fase *training* dan inferensi model AI skala besar itu sendiri memakan konsumsi energi listrik yang amat boros.
*   **Alokasi Sumber Daya Adil:** Memastikan model ML membagikan beban sumber daya yang efisien tanpa membebani infrastruktur *server* saat keadaan *idle/peak* belum matang sempurna.
*   **Sinkronisasi Terdistribusi:** Penerapan ML berbasis *cloud-edge* hibrida menuntut ketersambungan antar terminal, rawan terhadap masalah bias pengambilan keputusan trafik lokal vs global.

## Slide 10: Tren Masa Depan dalam Riset DCN
*   **Jaringan Otonom (DNOC):** Era *Dark Network Operation Centers*—pusat data cerdas yang dikendalikan penuh oleh mesin otonom tanpa memerlukan intervensi petugas manusia (*lights-out operation*).
*   **Kecerdasan *Edge* Terpadu:** Pemanfaatan AI-MEC (*Edge Computing*) dan AI-RAN untuk menjaga pemrosesan informasi tetap cepat di ujung terminal dekat dengan akses pengguna.
*   **Kriptografi Kuantum:** Penerapan jalur komunikasi super aman via komputasi kuantum demi membentengi arus vital DCN dari bahaya penyadapan *hacker*.
*   **Green AI:** Fokus utama penelitian beralih pada perancangan "AI Hijau"—algoritma model teringan yang membutuhkan rasio daya listrik dan jejak karbon terminim untuk beroperasi maksimal.

## Slide 11: Kesimpulan Akhir
*   Pergeseran arsitektur *Data Center Networks* mutlak tertuju pada adopsi sistem berbasis AI yang mandiri (*self-optimizing*) demi menjawab kebutuhan skala data masif.
*   Sistem AI secara menjanjikan mengatasi kendala utama DCN konvensional seperti kemacetan reaktif, efisiensi lalu lintas, dan analisis gangguan jaringan dini.
*   Tantangan pelik menyangkut minimnya basis data riil industri, konsumsi komputasi daya berat AI, dan celah ancaman peretasan *machine learning* harus segera dipecahkan.
*   **Arah Terdepan:** Kolaborasi pendekatan sistem hibrida—mensinergikan sisi cerdas adaptasi AI dengan efisiensi ringan komputasi jaringan tradisional—akan menjamin performa DCN paling tangguh dan pragmatis untuk masa depan kelak.
