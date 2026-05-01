# Laporan Analisis Paper: Optimization and Management of Data Center Networks

## Pendahuluan
Penelitian ini merupakan sebuah *scoping review* yang mengkaji secara komprehensif perkembangan terkini dalam optimalisasi dan manajemen Data Center Networks (DCN), dengan fokus khusus pada penerapan *Artificial Intelligence* (AI) dan *Machine Learning* (ML). Masalah utama (*Research Gap*) yang diidentifikasi adalah ketertinggalan arsitektur DCN tradisional dalam mengimbangi pertumbuhan eksponensial daya komputasi server. Hal ini menyebabkan terjadinya *bottleneck*, masalah latensi, dan transmisi data yang tidak efisien. Selain itu, kajian literatur sebelumnya cenderung berfokus pada aspek DCN secara terisolasi dan kurang menganalisis secara sistematis penerapan *end-to-end* AI/ML dalam memecahkan masalah kompleks di lingkungan DCN modern.

## Metodologi
Penelitian ini menggunakan metodologi terstruktur berbasis protokol PRISMA-ScR yang dikombinasikan dengan otomatisasi menggunakan *Large Language Models* (LLM). Langkah-langkah teknisnya meliputi:
1. **Identifikasi:** Pencarian komprehensif pada basis data akademik menggunakan kata kunci terkait DCN, menghasilkan 1.864 dokumen. Sebanyak 192 duplikat dihapus.
2. **Penyaringan (*Screening*):** Memanfaatkan pendekatan hibrida antara *skrip* berbasis API (CrossRef) untuk menyaring tipe akses dan tipe publikasi, serta LLM untuk ekstraksi tema otomatis. Proses ini menyisakan 1.660 dokumen studi.
3. **Uji Kelayakan (*Eligibility*):** LLM digunakan kembali untuk menguji apakah fokus utama dari setiap dokumen merupakan aplikasi pada DCN.
4. **Ekstraksi & Klasifikasi:** Menghasilkan 1.636 studi yang valid, yang kemudian dikategorikan ke dalam 7 tema riset utama.

## Hasil
Penelitian ini berhasil memetakan 7 domain utama riset DCN: *Optical Networking* (20%), *Fault Tolerance* (15%), *Energy-Efficient Management* (18%), *Congestion Control* (14%), *Flow Scheduling* (13%), *SDN* (12%), dan *Load Balancing* (8%). Perbandingan utama antara pendekatan AI dan konvensional adalah:
*   **Pendekatan Tradisional (84%):** Mengandalkan algoritma berbasis aturan (*rule-based*), konfigurasi statis, dan penyesuaian reaktif. Meskipun stabil dan efisien secara komputasi, pendekatan ini lambat dalam beradaptasi pada fluktuasi lalu lintas data dinamis.
*   **Pendekatan AI/ML (16%):** Menawarkan pengambilan keputusan *real-time*, analisis prediktif (seperti prediksi kegagalan jaringan), serta manajemen otonom. AI/ML lebih unggul dalam mengelola jaringan berskala besar, meskipun membutuhkan daya komputasi tinggi untuk tahap *training* dan inferensi.

## Analisis
Berdasarkan tinjauan kritis, paper ini memiliki beberapa batasan dan ruang untuk perbaikan (*Limitation/Kritik*):
1.  **Ketidaktersediaan Dataset:** Analisis menyoroti kelangkaan *dataset* DCN berkualitas tinggi dan *open-source* untuk melatih model AI. Sebagian besar *dataset* bersifat privat atau sintesis, yang berisiko tidak merepresentasikan lalu lintas jaringan riil.
2.  **Beban Komputasi AI:** Solusi AI/ML yang ditawarkan membutuhkan *resource* komputasi besar, yang berisiko meningkatkan konsumsi energi (*energy overhead*), berlawanan dengan tujuan utama *Green Computing* di *Data Center*.
3.  **Ancaman Keamanan Model AI:** Model ML rentan terhadap *adversarial attacks* (seperti *data poisoning*), yang dapat memanipulasi keputusan manajemen jaringan.
4.  **Keterbatasan Review:** Pengabaian paper berbahasa non-Inggris dan *closed-access* dapat menghilangkan wawasan dari penelitian-penelitian kunci di industri secara global. Secara keseluruhan, belum ditemukan *framework* AI terintegrasi yang benar-benar siap diterpakan secara *end-to-end* di industri.
