import os

base_path = os.getcwd()
image_path = str(base_path) + "/s.png"
data_db = str(base_path) + "/user_data.db"

cities = {'Port Blair': str(base_path) + '/city_sound/Port Blair.mp3',
          'Visakhapatnam': str(base_path) + '/city_sound/Visakhapatnam.mp3',
          'Vijayawada': str(base_path) + '/city_sound/Vijayawada.mp3',
          'Guntur': str(base_path) + '/city_sound/Guntur.mp3',
          'Nellore': str(base_path) + '/city_sound/Nellore.mp3',
          'Kurnool': str(base_path) + '/city_sound/Kurnool.mp3',
          'Rajamahendravaram': str(base_path) + '/city_sound/Rajamahendravaram.mp3',
          'Tirupati': str(base_path) + '/city_sound/Tirupati.mp3',
          'Kadapa': str(base_path) + '/city_sound/Kadapa.mp3',
          'Kakinada': str(base_path) + '/city_sound/Kakinada.mp3',
          'Anantapur': str(base_path) + '/city_sound/Anantapur.mp3',
          'Vizianagaram': str(base_path) + '/city_sound/Vizianagaram.mp3',
          'Eluru': str(base_path) + '/city_sound/Eluru.mp3',
          'Ongole': str(base_path) + '/city_sound/Ongole.mp3',
          'Nandyal': str(base_path) + '/city_sound/Nandyal.mp3',
          'Machilipatnam': str(base_path) + '/city_sound/Machilipatnam.mp3',
          'Adoni': str(base_path) + '/city_sound/Adoni.mp3',
          'Tenali': str(base_path) + '/city_sound/Tenali.mp3',
          'Proddatur': str(base_path) + '/city_sound/Proddatur.mp3',
          'Chittoor': str(base_path) + '/city_sound/Chittoor.mp3',
          'Hindupur': str(base_path) + '/city_sound/Hindupur.mp3',
          'Bhimavaram': str(base_path) + '/city_sound/Bhimavaram.mp3',
          'Madanapalle': str(base_path) + '/city_sound/Madanapalle.mp3',
          'Guntakal': str(base_path) + '/city_sound/Guntakal.mp3',
          'Srikakulam': str(base_path) + '/city_sound/Srikakulam.mp3',
          'Dharmavaram': str(base_path) + '/city_sound/Dharmavaram.mp3',
          'Gudivada': str(base_path) + '/city_sound/Gudivada.mp3',
          'Narasaraopet': str(base_path) + '/city_sound/Narasaraopet.mp3',
          'Tadipatri': str(base_path) + '/city_sound/Tadipatri.mp3',
          'Tadepalligudem': str(base_path) + '/city_sound/Tadepalligudem.mp3',
          'Amaravati': str(base_path) + '/city_sound/Amaravati.mp3',
          'Chilakaluripet': str(base_path) + '/city_sound/Chilakaluripet.mp3',
          'Itanagar': str(base_path) + '/city_sound/Itanagar.mp3',
          'Dhuburi': str(base_path) + '/city_sound/Dhuburi.mp3',
          'Dibrugarh': str(base_path) + '/city_sound/Dibrugarh.mp3',
          'Dispur': str(base_path) + '/city_sound/Dispur.mp3',
          'Guwahati': str(base_path) + '/city_sound/Guwahati.mp3',
          'Jorhat': str(base_path) + '/city_sound/Jorhat.mp3',
          'Nagaon': str(base_path) + '/city_sound/Nagaon.mp3',
          'Sivasagar': str(base_path) + '/city_sound/Sivasagar.mp3',
          'Silchar': str(base_path) + '/city_sound/Silchar.mp3',
          'Tezpur': str(base_path) + '/city_sound/Tezpur.mp3',
          'Tinsukia': str(base_path) + '/city_sound/Tinsukia.mp3',
          'Patna': str(base_path) + '/city_sound/Patna.mp3',
          'Gaya': str(base_path) + '/city_sound/Gaya.mp3',
          'Bhagalpur': str(base_path) + '/city_sound/Bhagalpur.mp3',
          'Muzaffarpur': str(base_path) + '/city_sound/Muzaffarpur.mp3',
          'Purnia': str(base_path) + '/city_sound/Purnia.mp3',
          'Darbhanga': str(base_path) + '/city_sound/Darbhanga.mp3',
          'Bihar Sharif': str(base_path) + '/city_sound/Bihar Sharif.mp3',
          'Arrah': str(base_path) + '/city_sound/Arrah.mp3',
          'Begusarai': str(base_path) + '/city_sound/Begusarai.mp3',
          'Katihar': str(base_path) + '/city_sound/Katihar.mp3',
          'Munger': str(base_path) + '/city_sound/Munger.mp3',
          'Chhapra': str(base_path) + '/city_sound/Chhapra.mp3',
          'Bettiah': str(base_path) + '/city_sound/Bettiah.mp3',
          'Saharsa': str(base_path) + '/city_sound/Saharsa.mp3',
          'Hajipur': str(base_path) + '/city_sound/Hajipur.mp3',
          'Sasaram': str(base_path) + '/city_sound/Sasaram.mp3',
          'Dehri': str(base_path) + '/city_sound/Dehri.mp3',
          'Siwan': str(base_path) + '/city_sound/Siwan.mp3',
          'Motihari': str(base_path) + '/city_sound/Motihari.mp3',
          'Nawada': str(base_path) + '/city_sound/Nawada.mp3',
          'Bagaha': str(base_path) + '/city_sound/Bagaha.mp3',
          'Buxar': str(base_path) + '/city_sound/Buxar.mp3',
          'Kishanganj': str(base_path) + '/city_sound/Kishanganj.mp3',
          'Sitamarhi': str(base_path) + '/city_sound/Sitamarhi.mp3',
          'Jamalpur': str(base_path) + '/city_sound/Jamalpur.mp3',
          'Jehanabad': str(base_path) + '/city_sound/Jehanabad.mp3',
          'Aurangabad': str(base_path) + '/city_sound/Aurangabad.mp3',
          'Lakhisarai': str(base_path) + '/city_sound/Lakhisarai.mp3',
          'Chandigarh': str(base_path) + '/city_sound/Chandigarh.mp3',
          'Raipur': str(base_path) + '/city_sound/Raipur.mp3',
          'Durg': str(base_path) + '/city_sound/Durg.mp3',
          'Naya Raipur': str(base_path) + '/city_sound/Naya Raipur.mp3',
          'Korba': str(base_path) + '/city_sound/Korba.mp3',
          'Bilaspur': str(base_path) + '/city_sound/Bilaspur.mp3',
          'Rajnandgaon': str(base_path) + '/city_sound/Rajnandgaon.mp3',
          'Pakhanjore': str(base_path) + '/city_sound/Pakhanjore.mp3',
          'Jagdalpur': str(base_path) + '/city_sound/Jagdalpur.mp3',
          'Ambikapur': str(base_path) + '/city_sound/Ambikapur.mp3',
          'Chirmiri': str(base_path) + '/city_sound/Chirmiri.mp3',
          'Dhamtari': str(base_path) + '/city_sound/Dhamtari.mp3',
          'Raigarh': str(base_path) + '/city_sound/Raigarh.mp3',
          'Mahasamund': str(base_path) + '/city_sound/Mahasamund.mp3',
          'Daman': str(base_path) + '/city_sound/Daman.mp3',
          'Delhi': str(base_path) + '/city_sound/Delhi.mp3',
          'Silvassa': str(base_path) + '/city_sound/Silvassa.mp3',
          'Panaji': str(base_path) + '/city_sound/Panaji.mp3',
          'Vasco': str(base_path) + '/city_sound/Vasco.mp3',
          'Mormugao': str(base_path) + '/city_sound/Mormugao.mp3',
          'Margao': str(base_path) + '/city_sound/Margao.mp3',
          'Ahmedabad': str(base_path) + '/city_sound/Ahmedabad.mp3',
          'Surat': str(base_path) + '/city_sound/Surat.mp3',
          'Vadodara': str(base_path) + '/city_sound/Vadodara.mp3',
          'Rajkot': str(base_path) + '/city_sound/Rajkot.mp3',
          'Bhavnagar': str(base_path) + '/city_sound/Bhavnagar.mp3',
          'Jamnagar': str(base_path) + '/city_sound/Jamnagar.mp3',
          'Junagadh': str(base_path) + '/city_sound/Junagadh.mp3',
          'Gandhidham': str(base_path) + '/city_sound/Gandhidham.mp3',
          'Nadiad': str(base_path) + '/city_sound/Nadiad.mp3',
          'Gandhinagar': str(base_path) + '/city_sound/Gandhinagar.mp3',
          'Anand': str(base_path) + '/city_sound/Anand.mp3',
          'Morbi': str(base_path) + '/city_sound/Morbi.mp3',
          'Khambhat': str(base_path) + '/city_sound/Khambhat.mp3',
          'Surendranagar': str(base_path) + '/city_sound/Surendranagar.mp3',
          'Bharuch': str(base_path) + '/city_sound/Bharuch.mp3',
          'Vapi': str(base_path) + '/city_sound/Vapi.mp3',
          'Navsari': str(base_path) + '/city_sound/Navsari.mp3',
          'Veraval': str(base_path) + '/city_sound/Veraval.mp3',
          'Porbandar': str(base_path) + '/city_sound/Porbandar.mp3',
          'Godhra': str(base_path) + '/city_sound/Godhra.mp3',
          'Bhuj': str(base_path) + '/city_sound/Bhuj.mp3',
          'Ankleshwar': str(base_path) + '/city_sound/Ankleshwar.mp3',
          'Botad': str(base_path) + '/city_sound/Botad.mp3',
          'Patan': str(base_path) + '/city_sound/Patan.mp3',
          'Palanpur': str(base_path) + '/city_sound/Palanpur.mp3',
          'Dahod': str(base_path) + '/city_sound/Dahod.mp3',
          'Jetpur': str(base_path) + '/city_sound/Jetpur.mp3',
          'Valsad': str(base_path) + '/city_sound/Valsad.mp3',
          'Kalol': str(base_path) + '/city_sound/Kalol.mp3',
          'Gondal': str(base_path) + '/city_sound/Gondal.mp3',
          'Deesa': str(base_path) + '/city_sound/Deesa.mp3',
          'Amreli': str(base_path) + '/city_sound/Amreli.mp3',
          'Mahuva': str(base_path) + '/city_sound/Mahuva.mp3',
          'Mehsana': str(base_path) + '/city_sound/Mehsana.mp3',
          'Shimla': str(base_path) + '/city_sound/Shimla.mp3',
          'Faridabad': str(base_path) + '/city_sound/Faridabad.mp3',
          'Gurgaon': str(base_path) + '/city_sound/Gurgaon.mp3',
          'Panipat': str(base_path) + '/city_sound/Panipat.mp3',
          'Ambala': str(base_path) + '/city_sound/Ambala.mp3',
          'Yamunanagar': str(base_path) + '/city_sound/Yamunanagar.mp3',
          'Rohtak': str(base_path) + '/city_sound/Rohtak.mp3',
          'Hisar': str(base_path) + '/city_sound/Hisar.mp3',
          'Karnal': str(base_path) + '/city_sound/Karnal.mp3',
          'Sonipat': str(base_path) + '/city_sound/Sonipat.mp3',
          'Panchkula': str(base_path) + '/city_sound/Panchkula.mp3',
          'Bhiwani': str(base_path) + '/city_sound/Bhiwani.mp3',
          'Sirsa': str(base_path) + '/city_sound/Sirsa.mp3',
          'Bahadurgarh': str(base_path) + '/city_sound/Bahadurgarh.mp3',
          'Jind': str(base_path) + '/city_sound/Jind.mp3',
          'Thanesar': str(base_path) + '/city_sound/Thanesar.mp3',
          'Kaithal': str(base_path) + '/city_sound/Kaithal.mp3',
          'Rewari': str(base_path) + '/city_sound/Rewari.mp3',
          'Palwal': str(base_path) + '/city_sound/Palwal.mp3',
          'Jamshedpur': str(base_path) + '/city_sound/Jamshedpur.mp3',
          'Dhanbad': str(base_path) + '/city_sound/Dhanbad.mp3',
          'Ranchi': str(base_path) + '/city_sound/Ranchi.mp3',
          'Bokaro Steel City': str(base_path) + '/city_sound/Bokaro Steel City.mp3',
          'Deoghar': str(base_path) + '/city_sound/Deoghar.mp3',
          'Phusro': str(base_path) + '/city_sound/Phusro.mp3',
          'Hazaribagh': str(base_path) + '/city_sound/Hazaribagh.mp3',
          'Giridih': str(base_path) + '/city_sound/Giridih.mp3',
          'Ramgarh': str(base_path) + '/city_sound/Ramgarh.mp3',
          'Medininagar': str(base_path) + '/city_sound/Medininagar.mp3',
          'Chirkunda': str(base_path) + '/city_sound/Chirkunda.mp3',
          'Jhumri Telaiya': str(base_path) + '/city_sound/Jhumri Telaiya.mp3',
          'Sahibganj': str(base_path) + '/city_sound/Sahibganj.mp3',
          'Srinagar': str(base_path) + '/city_sound/Srinagar.mp3',
          'Jammu': str(base_path) + '/city_sound/Jammu.mp3',
          'Anantnag': str(base_path) + '/city_sound/Anantnag.mp3',
          'Bengaluru': str(base_path) + '/city_sound/Bengaluru.mp3',
          'Hubli': str(base_path) + '/city_sound/Hubli.mp3',
          'Mysore': str(base_path) + '/city_sound/Mysore.mp3',
          'Gulbarga': str(base_path) + '/city_sound/Gulbarga.mp3',
          'Mangalore': str(base_path) + '/city_sound/Mangalore.mp3',
          'Belgaum': str(base_path) + '/city_sound/Belgaum.mp3',
          'Davangere': str(base_path) + '/city_sound/Davangere.mp3',
          'Bellary': str(base_path) + '/city_sound/Bellary.mp3',
          'Bijapur': str(base_path) + '/city_sound/Bijapur.mp3',
          'Shimoga': str(base_path) + '/city_sound/Shimoga.mp3',
          'Tumkur': str(base_path) + '/city_sound/Tumkur.mp3',
          'Raichur': str(base_path) + '/city_sound/Raichur.mp3',
          'Bidar': str(base_path) + '/city_sound/Bidar.mp3',
          'Hospet': str(base_path) + '/city_sound/Hospet.mp3',
          'Hassan': str(base_path) + '/city_sound/Hassan.mp3',
          'Gadag': str(base_path) + '/city_sound/Gadag.mp3',
          'Udupi': str(base_path) + '/city_sound/Udupi.mp3',
          'Robertsonpet': str(base_path) + '/city_sound/Robertsonpet.mp3',
          'Bhadravati': str(base_path) + '/city_sound/Bhadravati.mp3',
          'Chitradurga': str(base_path) + '/city_sound/Chitradurga.mp3',
          'Harihar': str(base_path) + '/city_sound/Harihar.mp3',
          'Kolar': str(base_path) + '/city_sound/Kolar.mp3',
          'Mandya': str(base_path) + '/city_sound/Mandya.mp3',
          'Chikkamagallooru': str(base_path) + '/city_sound/Chikkamagallooru.mp3',
          'Chikmagalur': str(base_path) + '/city_sound/Chikmagalur.mp3',
          'Gangawati': str(base_path) + '/city_sound/Gangawati.mp3',
          'Ranebennuru': str(base_path) + '/city_sound/Ranebennuru.mp3',
          'Ramanagara': str(base_path) + '/city_sound/Ramanagara.mp3',
          'Bagalkot': str(base_path) + '/city_sound/Bagalkot.mp3',
          'Thiruvananthapuram': str(base_path) + '/city_sound/Thiruvananthapuram.mp3',
          'Kochi': str(base_path) + '/city_sound/Kochi.mp3',
          'Calicut': str(base_path) + '/city_sound/Calicut.mp3',
          'Kollam': str(base_path) + '/city_sound/Kollam.mp3',
          'Thrissur': str(base_path) + '/city_sound/Thrissur.mp3',
          'Kannur': str(base_path) + '/city_sound/Kannur.mp3',
          'Kasaragod': str(base_path) + '/city_sound/Kasaragod.mp3',
          'Alappuzha': str(base_path) + '/city_sound/Alappuzha.mp3',
          'Palakkad': str(base_path) + '/city_sound/Palakkad.mp3',
          'Kottayam': str(base_path) + '/city_sound/Kottayam.mp3',
          'Kothamangalam': str(base_path) + '/city_sound/Kothamangalam.mp3',
          'Malappuram': str(base_path) + '/city_sound/Malappuram.mp3',
          'Manjeri': str(base_path) + '/city_sound/Manjeri.mp3',
          'Thalassery': str(base_path) + '/city_sound/Thalassery.mp3',
          'Ponnani': str(base_path) + '/city_sound/Ponnani.mp3',
          'Kavaratti': str(base_path) + '/city_sound/Kavaratti.mp3',
          'Mumbai': str(base_path) + '/city_sound/Mumbai.mp3',
          'Pune': str(base_path) + '/city_sound/Pune.mp3',
          'Nagpur': str(base_path) + '/city_sound/Nagpur.mp3',
          'Nashik': str(base_path) + '/city_sound/Nashik.mp3',
          'Pimpri-Chinchwad': str(base_path) + '/city_sound/Pimpri-Chinchwad.mp3',
          'Solapur': str(base_path) + '/city_sound/Solapur.mp3',
          'Bhiwandi': str(base_path) + '/city_sound/Bhiwandi.mp3',
          'Amravati': str(base_path) + '/city_sound/Amravati.mp3',
          'Nanded': str(base_path) + '/city_sound/Nanded.mp3',
          'Kolhapur': str(base_path) + '/city_sound/Kolhapur.mp3',
          'Sangli-Miraj-Kupwad': str(base_path) + '/city_sound/Sangli-Miraj-Kupwad.mp3',
          'Jalgaon': str(base_path) + '/city_sound/Jalgaon.mp3',
          'Akola': str(base_path) + '/city_sound/Akola.mp3',
          'Latur': str(base_path) + '/city_sound/Latur.mp3',
          'Malegaon': str(base_path) + '/city_sound/Malegaon.mp3',
          'Dhule': str(base_path) + '/city_sound/Dhule.mp3',
          'Ahmednagar': str(base_path) + '/city_sound/Ahmednagar.mp3',
          'Nandurbar': str(base_path) + '/city_sound/Nandurbar.mp3',
          'Ichalkaranji': str(base_path) + '/city_sound/Ichalkaranji.mp3',
          'Chandrapur': str(base_path) + '/city_sound/Chandrapur.mp3',
          'Jalna': str(base_path) + '/city_sound/Jalna.mp3',
          'Parbhani': str(base_path) + '/city_sound/Parbhani.mp3',
          'Bhusawal': str(base_path) + '/city_sound/Bhusawal.mp3',
          'Satara': str(base_path) + '/city_sound/Satara.mp3',
          'Beed': str(base_path) + '/city_sound/Beed.mp3',
          'Pandharpur': str(base_path) + '/city_sound/Pandharpur.mp3',
          'Yavatmal': str(base_path) + '/city_sound/Yavatmal.mp3',
          'Kamptee': str(base_path) + '/city_sound/Kamptee.mp3',
          'Gondia': str(base_path) + '/city_sound/Gondia.mp3',
          'Achalpur': str(base_path) + '/city_sound/Achalpur.mp3',
          'Osmanabad': str(base_path) + '/city_sound/Osmanabad.mp3',
          'Hinganghat': str(base_path) + '/city_sound/Hinganghat.mp3',
          'Wardha': str(base_path) + '/city_sound/Wardha.mp3',
          'Barshi': str(base_path) + '/city_sound/Barshi.mp3',
          'Chalisgaon': str(base_path) + '/city_sound/Chalisgaon.mp3',
          'Amalner': str(base_path) + '/city_sound/Amalner.mp3',
          'Khamgaon': str(base_path) + '/city_sound/Khamgaon.mp3',
          'Akot': str(base_path) + '/city_sound/Akot.mp3',
          'Udgir': str(base_path) + '/city_sound/Udgir.mp3',
          'Bhandara': str(base_path) + '/city_sound/Bhandara.mp3',
          'Parli': str(base_path) + '/city_sound/Parli.mp3',
          'Shillong': str(base_path) + '/city_sound/Shillong.mp3',
          'Imphal': str(base_path) + '/city_sound/Imphal.mp3',
          'Indore': str(base_path) + '/city_sound/Indore.mp3',
          'Bhopal': str(base_path) + '/city_sound/Bhopal.mp3',
          'Jabalpur': str(base_path) + '/city_sound/Jabalpur.mp3',
          'Gwalior': str(base_path) + '/city_sound/Gwalior.mp3',
          'Ujjain': str(base_path) + '/city_sound/Ujjain.mp3',
          'Sagar': str(base_path) + '/city_sound/Sagar.mp3',
          'Dewas': str(base_path) + '/city_sound/Dewas.mp3',
          'Satna': str(base_path) + '/city_sound/Satna.mp3',
          'Ratlam': str(base_path) + '/city_sound/Ratlam.mp3',
          'Rewa': str(base_path) + '/city_sound/Rewa.mp3',
          'Katni': str(base_path) + '/city_sound/Katni.mp3',
          'Singrauli': str(base_path) + '/city_sound/Singrauli.mp3',
          'Burhanpur': str(base_path) + '/city_sound/Burhanpur.mp3',
          'Khandwa': str(base_path) + '/city_sound/Khandwa.mp3',
          'Morena': str(base_path) + '/city_sound/Morena.mp3',
          'Bhind': str(base_path) + '/city_sound/Bhind.mp3',
          'Chhindwara': str(base_path) + '/city_sound/Chhindwara.mp3',
          'Guna': str(base_path) + '/city_sound/Guna.mp3',
          'Shivpuri': str(base_path) + '/city_sound/Shivpuri.mp3',
          'Vidisha': str(base_path) + '/city_sound/Vidisha.mp3',
          'Chhatarpur': str(base_path) + '/city_sound/Chhatarpur.mp3',
          'Damoh': str(base_path) + '/city_sound/Damoh.mp3',
          'Mandsaur': str(base_path) + '/city_sound/Mandsaur.mp3',
          'Khargone': str(base_path) + '/city_sound/Khargone.mp3',
          'Neemuch': str(base_path) + '/city_sound/Neemuch.mp3',
          'Pithampur': str(base_path) + '/city_sound/Pithampur.mp3',
          'Hoshangabad': str(base_path) + '/city_sound/Hoshangabad.mp3',
          'Itarsi': str(base_path) + '/city_sound/Itarsi.mp3',
          'Sehore': str(base_path) + '/city_sound/Sehore.mp3',
          'Betul': str(base_path) + '/city_sound/Betul.mp3',
          'Seoni': str(base_path) + '/city_sound/Seoni.mp3',
          'Datia': str(base_path) + '/city_sound/Datia.mp3',
          'Nagda': str(base_path) + '/city_sound/Nagda.mp3',
          'Dhanpuri': str(base_path) + '/city_sound/Dhanpuri.mp3',
          'Dhar': str(base_path) + '/city_sound/Dhar.mp3',
          'Balaghat': str(base_path) + '/city_sound/Balaghat.mp3',
          'Aizawl': str(base_path) + '/city_sound/Aizawl.mp3',
          'Dimapur': str(base_path) + '/city_sound/Dimapur.mp3',
          'Kohima': str(base_path) + '/city_sound/Kohima.mp3',
          'Bhubaneswar': str(base_path) + '/city_sound/Bhubaneswar.mp3',
          'Cuttack': str(base_path) + '/city_sound/Cuttack.mp3',
          'Rourkela': str(base_path) + '/city_sound/Rourkela.mp3',
          'Berhampur': str(base_path) + '/city_sound/Berhampur.mp3',
          'Sambalpur': str(base_path) + '/city_sound/Sambalpur.mp3',
          'Puri': str(base_path) + '/city_sound/Puri.mp3',
          'Balasore': str(base_path) + '/city_sound/Balasore.mp3',
          'Bhadrak': str(base_path) + '/city_sound/Bhadrak.mp3',
          'Baripada': str(base_path) + '/city_sound/Baripada.mp3',
          'Balangir': str(base_path) + '/city_sound/Balangir.mp3',
          'Jharsuguda': str(base_path) + '/city_sound/Jharsuguda.mp3',
          'Jeypore': str(base_path) + '/city_sound/Jeypore.mp3',
          'Ludhiana': str(base_path) + '/city_sound/Ludhiana.mp3',
          'Amritsar': str(base_path) + '/city_sound/Amritsar.mp3',
          'Jalandhar': str(base_path) + '/city_sound/Jalandhar.mp3',
          'Patiala': str(base_path) + '/city_sound/Patiala.mp3',
          'Bathinda': str(base_path) + '/city_sound/Bathinda.mp3',
          'Hoshiarpur': str(base_path) + '/city_sound/Hoshiarpur.mp3',
          'Batala': str(base_path) + '/city_sound/Batala.mp3',
          'Mohali': str(base_path) + '/city_sound/Mohali.mp3',
          'Abohar': str(base_path) + '/city_sound/Abohar.mp3',
          'Pathankot': str(base_path) + '/city_sound/Pathankot.mp3',
          'Moga': str(base_path) + '/city_sound/Moga.mp3',
          'Malerkotla': str(base_path) + '/city_sound/Malerkotla.mp3',
          'Khanna': str(base_path) + '/city_sound/Khanna.mp3',
          'Muktasar': str(base_path) + '/city_sound/Muktasar.mp3',
          'Barnala': str(base_path) + '/city_sound/Barnala.mp3',
          'Firozpur': str(base_path) + '/city_sound/Firozpur.mp3',
          'Kapurthala': str(base_path) + '/city_sound/Kapurthala.mp3',
          'Phagwara': str(base_path) + '/city_sound/Phagwara.mp3',
          'Zirakpur': str(base_path) + '/city_sound/Zirakpur.mp3',
          'Rajpura': str(base_path) + '/city_sound/Rajpura.mp3',
          'Pondicherry': str(base_path) + '/city_sound/Pondicherry.mp3',
          'Ozhukarai': str(base_path) + '/city_sound/Ozhukarai.mp3',
          'Karaikal': str(base_path) + '/city_sound/Karaikal.mp3',
          'Jaipur': str(base_path) + '/city_sound/Jaipur.mp3',
          'Jodhpur': str(base_path) + '/city_sound/Jodhpur.mp3',
          'Kota': str(base_path) + '/city_sound/Kota.mp3',
          'Bikaner': str(base_path) + '/city_sound/Bikaner.mp3',
          'Ajmer': str(base_path) + '/city_sound/Ajmer.mp3',
          'Udaipur': str(base_path) + '/city_sound/Udaipur.mp3',
          'Bhilwara': str(base_path) + '/city_sound/Bhilwara.mp3',
          'Alwar': str(base_path) + '/city_sound/Alwar.mp3',
          'Bharatpur': str(base_path) + '/city_sound/Bharatpur.mp3',
          'Sri Ganganagar': str(base_path) + '/city_sound/Sri Ganganagar.mp3',
          'Sikar': str(base_path) + '/city_sound/Sikar.mp3',
          'Pali': str(base_path) + '/city_sound/Pali.mp3',
          'Barmer': str(base_path) + '/city_sound/Barmer.mp3',
          'Tonk': str(base_path) + '/city_sound/Tonk.mp3',
          'Kishangarh': str(base_path) + '/city_sound/Kishangarh.mp3',
          'Chittorgarh': str(base_path) + '/city_sound/Chittorgarh.mp3',
          'Beawar': str(base_path) + '/city_sound/Beawar.mp3',
          'Hanumangarh': str(base_path) + '/city_sound/Hanumangarh.mp3',
          'Dholpur': str(base_path) + '/city_sound/Dholpur.mp3',
          'Gangapur': str(base_path) + '/city_sound/Gangapur.mp3',
          'Sawai Madhopur': str(base_path) + '/city_sound/Sawai Madhopur.mp3',
          'Churu': str(base_path) + '/city_sound/Churu.mp3',
          'Baran': str(base_path) + '/city_sound/Baran.mp3',
          'Makrana': str(base_path) + '/city_sound/Makrana.mp3',
          'Nagaur': str(base_path) + '/city_sound/Nagaur.mp3',
          'Hindaun': str(base_path) + '/city_sound/Hindaun.mp3',
          'Bhiwadi': str(base_path) + '/city_sound/Bhiwadi.mp3',
          'Bundi': str(base_path) + '/city_sound/Bundi.mp3',
          'Sujangarh': str(base_path) + '/city_sound/Sujangarh.mp3',
          'Jhunjhunu': str(base_path) + '/city_sound/Jhunjhunu.mp3',
          'Banswara': str(base_path) + '/city_sound/Banswara.mp3',
          'Sardarshahar': str(base_path) + '/city_sound/Sardarshahar.mp3',
          'Fatehpur': str(base_path) + '/city_sound/Fatehpur.mp3',
          'Dausa': str(base_path) + '/city_sound/Dausa.mp3',
          'Karauli': str(base_path) + '/city_sound/Karauli.mp3',
          'Gangtok': str(base_path) + '/city_sound/Gangtok.mp3',
          'Hyderabad': str(base_path) + '/city_sound/Hyderabad.mp3',
          'Warangal': str(base_path) + '/city_sound/Warangal.mp3',
          'Nizamabad': str(base_path) + '/city_sound/Nizamabad.mp3',
          'Karimnagar': str(base_path) + '/city_sound/Karimnagar.mp3',
          'Ramagundam': str(base_path) + '/city_sound/Ramagundam.mp3',
          'Khammam': str(base_path) + '/city_sound/Khammam.mp3',
          'Mahbubnagar': str(base_path) + '/city_sound/Mahbubnagar.mp3',
          'Nalgonda': str(base_path) + '/city_sound/Nalgonda.mp3',
          'Adilabad': str(base_path) + '/city_sound/Adilabad.mp3',
          'Siddipet': str(base_path) + '/city_sound/Siddipet.mp3',
          'Suryapet': str(base_path) + '/city_sound/Suryapet.mp3',
          'Miryalaguda': str(base_path) + '/city_sound/Miryalaguda.mp3',
          'Jagtial': str(base_path) + '/city_sound/Jagtial.mp3',
          'Mancherial': str(base_path) + '/city_sound/Mancherial.mp3',
          'Kothagudem': str(base_path) + '/city_sound/Kothagudem.mp3',
          'Chennai': str(base_path) + '/city_sound/Chennai.mp3',
          'Coimbatore': str(base_path) + '/city_sound/Coimbatore.mp3',
          'Madurai': str(base_path) + '/city_sound/Madurai.mp3',
          'Tiruchirappalli': str(base_path) + '/city_sound/Tiruchirappalli.mp3',
          'Tirupur': str(base_path) + '/city_sound/Tirupur.mp3',
          'Salem': str(base_path) + '/city_sound/Salem.mp3',
          'Erode': str(base_path) + '/city_sound/Erode.mp3',
          'Tirunelveli': str(base_path) + '/city_sound/Tirunelveli.mp3',
          'Vellore': str(base_path) + '/city_sound/Vellore.mp3',
          'Tuticorin': str(base_path) + '/city_sound/Tuticorin.mp3',
          'Gudiyatham': str(base_path) + '/city_sound/Gudiyatham.mp3',
          'Nagercoil': str(base_path) + '/city_sound/Nagercoil.mp3',
          'Thanjavur': str(base_path) + '/city_sound/Thanjavur.mp3',
          'Dindigul': str(base_path) + '/city_sound/Dindigul.mp3',
          'Vaniyambadi': str(base_path) + '/city_sound/Vaniyambadi.mp3',
          'Cuddalore': str(base_path) + '/city_sound/Cuddalore.mp3',
          'Komarapalayam': str(base_path) + '/city_sound/Komarapalayam.mp3',
          'Kanchipuram': str(base_path) + '/city_sound/Kanchipuram.mp3',
          'Ambur': str(base_path) + '/city_sound/Ambur.mp3',
          'Tiruvannamalai': str(base_path) + '/city_sound/Tiruvannamalai.mp3',
          'Pudukkottai': str(base_path) + '/city_sound/Pudukkottai.mp3',
          'Kumbakonam': str(base_path) + '/city_sound/Kumbakonam.mp3',
          'Rajapalayam': str(base_path) + '/city_sound/Rajapalayam.mp3',
          'Hosur': str(base_path) + '/city_sound/Hosur.mp3',
          'Karaikudi': str(base_path) + '/city_sound/Karaikudi.mp3',
          'Neyveli': str(base_path) + '/city_sound/Neyveli.mp3',
          'Nagapattinam': str(base_path) + '/city_sound/Nagapattinam.mp3',
          'Viluppuram': str(base_path) + '/city_sound/Viluppuram.mp3',
          'Paramakudi': str(base_path) + '/city_sound/Paramakudi.mp3',
          'Tiruchengode': str(base_path) + '/city_sound/Tiruchengode.mp3',
          'Kovilpatti': str(base_path) + '/city_sound/Kovilpatti.mp3',
          'Theni-Allinagaram': str(base_path) + '/city_sound/Theni-Allinagaram.mp3',
          'Kadayanallur': str(base_path) + '/city_sound/Kadayanallur.mp3',
          'Pollachi': str(base_path) + '/city_sound/Pollachi.mp3',
          'Ooty': str(base_path) + '/city_sound/Ooty.mp3',
          'Agartala': str(base_path) + '/city_sound/Agartala.mp3',
          'Kanpur': str(base_path) + '/city_sound/Kanpur.mp3',
          'Lucknow': str(base_path) + '/city_sound/Lucknow.mp3',
          'Ghaziabad': str(base_path) + '/city_sound/Ghaziabad.mp3',
          'Agra': str(base_path) + '/city_sound/Agra.mp3',
          'Varanasi': str(base_path) + '/city_sound/Varanasi.mp3',
          'Meerut': str(base_path) + '/city_sound/Meerut.mp3',
          'Allahabad': str(base_path) + '/city_sound/Allahabad.mp3',
          'Bareilly': str(base_path) + '/city_sound/Bareilly.mp3',
          'Aligarh': str(base_path) + '/city_sound/Aligarh.mp3',
          'Moradabad': str(base_path) + '/city_sound/Moradabad.mp3',
          'Saharanpur': str(base_path) + '/city_sound/Saharanpur.mp3',
          'Gorakhpur': str(base_path) + '/city_sound/Gorakhpur.mp3',
          'Faizabad': str(base_path) + '/city_sound/Faizabad.mp3',
          'Firozabad': str(base_path) + '/city_sound/Firozabad.mp3',
          'Jhansi': str(base_path) + '/city_sound/Jhansi.mp3',
          'Muzaffarnagar': str(base_path) + '/city_sound/Muzaffarnagar.mp3',
          'Mathura': str(base_path) + '/city_sound/Mathura.mp3',
          'Budaun': str(base_path) + '/city_sound/Budaun.mp3',
          'Rampur': str(base_path) + '/city_sound/Rampur.mp3',
          'Shahjahanpur': str(base_path) + '/city_sound/Shahjahanpur.mp3',
          'Farrukhabad': str(base_path) + '/city_sound/Farrukhabad.mp3',
          'Mau': str(base_path) + '/city_sound/Mau.mp3',
          'Hapur': str(base_path) + '/city_sound/Hapur.mp3',
          'Noida': str(base_path) + '/city_sound/Noida.mp3',
          'Etawah': str(base_path) + '/city_sound/Etawah.mp3',
          'Mirzapur': str(base_path) + '/city_sound/Mirzapur.mp3',
          'Bulandshahr': str(base_path) + '/city_sound/Bulandshahr.mp3',
          'Sambhal': str(base_path) + '/city_sound/Sambhal.mp3',
          'Amroha': str(base_path) + '/city_sound/Amroha.mp3',
          'Hardoi': str(base_path) + '/city_sound/Hardoi.mp3',
          'Raebareli': str(base_path) + '/city_sound/Raebareli.mp3',
          'Orai': str(base_path) + '/city_sound/Orai.mp3',
          'Sitapur': str(base_path) + '/city_sound/Sitapur.mp3',
          'Bahraich': str(base_path) + '/city_sound/Bahraich.mp3',
          'Modinagar': str(base_path) + '/city_sound/Modinagar.mp3',
          'Unnao': str(base_path) + '/city_sound/Unnao.mp3',
          'Jaunpur': str(base_path) + '/city_sound/Jaunpur.mp3',
          'Lakhimpur': str(base_path) + '/city_sound/Lakhimpur.mp3',
          'Hathras': str(base_path) + '/city_sound/Hathras.mp3',
          'Banda': str(base_path) + '/city_sound/Banda.mp3',
          'Pilibhit': str(base_path) + '/city_sound/Pilibhit.mp3',
          'Barabanki': str(base_path) + '/city_sound/Barabanki.mp3',
          'Mughalsarai': str(base_path) + '/city_sound/Mughalsarai.mp3',
          'Khurja': str(base_path) + '/city_sound/Khurja.mp3',
          'Gonda': str(base_path) + '/city_sound/Gonda.mp3',
          'Mainpuri': str(base_path) + '/city_sound/Mainpuri.mp3',
          'Lalitpur': str(base_path) + '/city_sound/Lalitpur.mp3',
          'Etah': str(base_path) + '/city_sound/Etah.mp3',
          'Deoria': str(base_path) + '/city_sound/Deoria.mp3',
          'Ujhani': str(base_path) + '/city_sound/Ujhani.mp3',
          'Ghazipur': str(base_path) + '/city_sound/Ghazipur.mp3',
          'Sultanpur': str(base_path) + '/city_sound/Sultanpur.mp3',
          'Azamgarh': str(base_path) + '/city_sound/Azamgarh.mp3',
          'Bijnor': str(base_path) + '/city_sound/Bijnor.mp3',
          'Sahaswan': str(base_path) + '/city_sound/Sahaswan.mp3',
          'Basti': str(base_path) + '/city_sound/Basti.mp3',
          'Chandausi': str(base_path) + '/city_sound/Chandausi.mp3',
          'Akbarpur': str(base_path) + '/city_sound/Akbarpur.mp3',
          'Ballia': str(base_path) + '/city_sound/Ballia.mp3',
          'Mubarakpur': str(base_path) + '/city_sound/Mubarakpur.mp3',
          'Tanda': str(base_path) + '/city_sound/Tanda.mp3',
          'Greater Noida': str(base_path) + '/city_sound/Greater Noida.mp3',
          'Shikohabad': str(base_path) + '/city_sound/Shikohabad.mp3',
          'Shamli': str(base_path) + '/city_sound/Shamli.mp3',
          'Baraut': str(base_path) + '/city_sound/Baraut.mp3',
          'Khair': str(base_path) + '/city_sound/Khair.mp3',
          'Kasganj': str(base_path) + '/city_sound/Kasganj.mp3',
          'Auraiya': str(base_path) + '/city_sound/Auraiya.mp3',
          'Khatauli': str(base_path) + '/city_sound/Khatauli.mp3',
          'Deoband': str(base_path) + '/city_sound/Deoband.mp3',
          'Nagina': str(base_path) + '/city_sound/Nagina.mp3',
          'Mahoba': str(base_path) + '/city_sound/Mahoba.mp3',
          'Muradnagar': str(base_path) + '/city_sound/Muradnagar.mp3',
          'Bhadohi': str(base_path) + '/city_sound/Bhadohi.mp3',
          'Dadri': str(base_path) + '/city_sound/Dadri.mp3',
          'Pratapgarh': str(base_path) + '/city_sound/Pratapgarh.mp3',
          'Najibabad': str(base_path) + '/city_sound/Najibabad.mp3',
          'Dehradun': str(base_path) + '/city_sound/Dehradun.mp3',
          'Haridwar': str(base_path) + '/city_sound/Haridwar.mp3',
          'Roorkee': str(base_path) + '/city_sound/Roorkee.mp3',
          'Haldwani': str(base_path) + '/city_sound/Haldwani.mp3',
          'Rudrapur': str(base_path) + '/city_sound/Rudrapur.mp3',
          'Kashipur': str(base_path) + '/city_sound/Kashipur.mp3',
          'Rishikesh': str(base_path) + '/city_sound/Rishikesh.mp3',
          'Kolkata': str(base_path) + '/city_sound/Kolkata.mp3',
          'Asansol': str(base_path) + '/city_sound/Asansol.mp3',
          'Siliguri': str(base_path) + '/city_sound/Siliguri.mp3',
          'Durgapur': str(base_path) + '/city_sound/Durgapur.mp3',
          'Bardhaman': str(base_path) + '/city_sound/Bardhaman.mp3',
          'Malda': str(base_path) + '/city_sound/Malda.mp3',
          'Baharampur': str(base_path) + '/city_sound/Baharampur.mp3',
          'Habra': str(base_path) + '/city_sound/Habra.mp3',
          'Jalpaiguri': str(base_path) + '/city_sound/Jalpaiguri.mp3',
          'Kharagpur': str(base_path) + '/city_sound/Kharagpur.mp3',
          'Shantipur': str(base_path) + '/city_sound/Shantipur.mp3',
          'Dankuni': str(base_path) + '/city_sound/Dankuni.mp3',
          'Dhulian': str(base_path) + '/city_sound/Dhulian.mp3',
          'Ranaghat': str(base_path) + '/city_sound/Ranaghat.mp3',
          'Haldia': str(base_path) + '/city_sound/Haldia.mp3',
          'Raiganj': str(base_path) + '/city_sound/Raiganj.mp3',
          'Krishnanagar': str(base_path) + '/city_sound/Krishnanagar.mp3',
          'Nabadwip': str(base_path) + '/city_sound/Nabadwip.mp3',
          'Midnapore': str(base_path) + '/city_sound/Midnapore.mp3',
          'Balurghat': str(base_path) + '/city_sound/Balurghat.mp3',
          'Basirhat': str(base_path) + '/city_sound/Basirhat.mp3',
          'Bankura': str(base_path) + '/city_sound/Bankura.mp3',
          'Chakdaha': str(base_path) + '/city_sound/Chakdaha.mp3',
          'Darjeeling': str(base_path) + '/city_sound/Darjeeling.mp3',
          'Alipurduar': str(base_path) + '/city_sound/Alipurduar.mp3',
          'Purulia': str(base_path) + '/city_sound/Purulia.mp3',
          'Jangipur': str(base_path) + '/city_sound/Jangipur.mp3',
          'Bangaon': str(base_path) + '/city_sound/Bangaon.mp3',
          'Cooch Behar': str(base_path) + '/city_sound/Cooch Behar.mp3',
          'Bolpur': str(base_path) + '/city_sound/Bolpur.mp3',
          'Kanthi': str(base_path) + '/city_sound/Kanthi.mp3'}

city_names = sorted(list(cities.keys()))

train_type = {"express": str(base_path) + "/type/express.mp3",
              "superfast": str(base_path) + "/type/superfast.wav",
              "shatabdi": str(base_path) + "/type/shatabdi.mp3",
              "passenger": str(base_path) + "/type/passenger.mp3"}
lst_train_type = sorted(list(train_type.keys()))

# english anouncement
eng_num = {"0": str(base_path) + "/english/0_eng.mp3", "1": str(base_path) + "/english/1_eng.mp3",
           "2": str(base_path) + "/english/2_eng.wav", "3": str(base_path) + "/english/3_eng.wav",
           "4": str(base_path) + "/english/4_eng.mp3", "5": str(base_path) + "/english/5_eng.mp3",
           "6": str(base_path) + "/english/6_eng.wav", "7": str(base_path) + "/english/7_eng.mp3",
           "8": str(base_path) + "/english/8_eng.mp3", "9": str(base_path) + "/english/9_eng.mp3"}
eng_start = str(base_path) + "/english/eng_start.mp3"
eng_out_arv = str(base_path) + "/english/outro_arv_eng.mp3"
eng_out_dep_1 = str(base_path) + "/english/outro_dep_eng_1.wav"
eng_out_dep_2 = str(base_path) + "/english/outro_dep_eng_2.wav"
eng_to = str(base_path) + '/english/to.mp3'

# hindi anouncement
hindi_start = str(base_path) + "/hindi/intro hindi.mp3"
hindi_out = str(base_path) + "/hindi/outro_arv_1_hn.wav"
hindi_out_dep = str(base_path) + "/hindi/outro_dep_hin_2.wav"
hindi_out_arv = str(base_path) + "/hindi/outro_arv_2_hn.wav"
hindi_num = {"0": str(base_path) + "/hindi/0_hin.wav", "1": str(base_path) + "/hindi/1_mar.mp3",
             "2": str(base_path) + "/hindi/2_hin.wav", "3": str(base_path) + "/hindi/3_mar.wav",
             "4": str(base_path) + "/hindi/4_mar.mp3", "5": str(base_path) + "/hindi/5_mar.mp3",
             "6": str(base_path) + "/hindi/6_hin.wav", "7": str(base_path) + "/hindi/7_mar.mp3",
             "8": str(base_path) + "/hindi/8_mar.mp3", "9": str(base_path) + "/hindi/9_mar.mp3"}
hi_se = str(base_path) + '/hindi/se.mp3'
jane_wali = str(base_path) + '/hindi/jane_vali.mp3'

# gujrati announcement
guj_num = {"0": str(base_path) + "/gujrati/1.mp3", "1": str(base_path) + "/gujrati/1.mp3",
           "2": str(base_path) + "/gujrati/2.mp3", "3": str(base_path) + "/gujrati/3.mp3",
           "4": str(base_path) + "/gujrati/4.mp3", "5": str(base_path) + "/gujrati/5.mp3",
           "6": str(base_path) + "/gujrati/6.mp3", "7": str(base_path) + "/gujrati/7.mp3",
           "8": str(base_path) + "/gujrati/8.mp3", "9": str(base_path) + "/gujrati/9.mp3"}
guj_start = str(base_path) + '/gujrati/guj_intro.mp3'
guj_out_dep = str(base_path) + '/gujrati/guj_out_dep.mp3'
guj_out_arv = str(base_path) + '/gujrati/guj_out_arv.mp3'
guj_thi = str(base_path) + '/gujrati/thi.mp3'
guj_java_vali = str(base_path) + '/gujrati/java_vali.mp3'
guj_gadi = str(base_path) + '/gujrati/gadi_sankhya.mp3'
train_number = str(base_path) + '/gujrati/train_num.mp3'
platform_num_guj = str(base_path) + '/gujrati/platform_num_guj.mp3'

bell_start = str(base_path) + '/bell_start.mp3'
bell_end = str(base_path) + "/railway_sms.mp3"
bell2 = str(base_path) + "/smoke.mp3"
bell3 = str(base_path) + "/last bell.mp3"
