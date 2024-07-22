Cara Kerja Ansible
Ansible adalah alat otomatisasi open-source yang digunakan untuk konfigurasi, manajemen, dan penyebaran aplikasi. Ansible bekerja dengan cara menghubungkan ke node (komputer) melalui SSH dan mendorong konfigurasi dari satu titik pusat (control node).

Komponen-Komponen Ansible
Playbooks:

Definisi: Playbooks adalah file YAML yang mendefinisikan serangkaian tugas yang harus dijalankan pada host yang dikelola.
Fungsi: Mengandung instruksi terstruktur dalam bentuk plays yang mendefinisikan tugas yang akan dieksekusi.
Inventory:

Definisi: Inventory adalah file yang menyimpan daftar host yang akan dikelola oleh Ansible.
Fungsi: Menyediakan informasi tentang sistem target. Inventory bisa dalam bentuk file statis atau dynamic inventory script yang menghasilkan daftar host secara dinamis.
Modules:

Definisi: Modules adalah unit dari kode yang berfungsi sebagai blok bangunan tugas dalam Playbooks.
Fungsi: Menyediakan kemampuan untuk menjalankan tugas spesifik, seperti menginstal paket, mengelola file, dan banyak lagi.
Perbandingan Terraform dan Ansible
Kelebihan dan Kekurangan
Terraform:

Kelebihan:
Idempotensi: Mendukung deklarasi infrastruktur sebagai kode (IaC) yang memungkinkan untuk menentukan keadaan akhir yang diinginkan.
State Management: Terraform menjaga state file yang merekam keadaan infrastruktur.
Provider Ecosystem: Mendukung berbagai provider (AWS, GCP, Azure, dll).
Kekurangan:
Learning Curve: Membutuhkan waktu untuk memahami konsep state dan HCL (HashiCorp Configuration Language).
Deployment Focused: Lebih fokus pada provisioning daripada konfigurasi.
Ansible:

Kelebihan:
Agentless: Tidak memerlukan agen yang berjalan di host target, hanya menggunakan SSH.
Simplicity: Mudah dipelajari dan digunakan karena menggunakan YAML untuk penulisan Playbooks.
Versatile: Dapat digunakan untuk konfigurasi, deployment, dan manajemen.
Kekurangan:
Scalability: Dapat menghadapi masalah skalabilitas pada infrastruktur yang sangat besar.
No State Management: Tidak menyimpan state dari infrastruktur, sehingga tidak mendukung idempotensi sebaik Terraform.
Use Case dan Skenario
Terraform:

Use Case: Membangun dan mengelola infrastruktur cloud (seperti VM, VPC, dan layanan cloud lainnya).
Skenario: Provisioning resource cloud di AWS, GCP, atau Azure dengan mendefinisikan infrastruktur sebagai kode.
Ansible:

Use Case: Konfigurasi dan manajemen server, deployment aplikasi, dan pengelolaan tugas berulang.
Skenario: Mengkonfigurasi server web dengan Nginx, menerapkan pembaruan keamanan, atau mengelola konfigurasi aplikasi.
Dengan memahami kedua tools ini, kamu bisa memilih alat yang tepat sesuai dengan kebutuhan spesifik dari infrastruktur dan aplikasi yang dikelola.
