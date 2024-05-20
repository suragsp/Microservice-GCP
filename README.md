# Microservice-GCP
Above given are the files we can use for setting up a Microservice-GCP. Here i have also added a HTML page which will help to upload the files online on the GCP.
Step 1: You need to have Google Cloud Account- <a href="https://console.cloud.google.com/freetrial/signup"> Signup</a>
Once done you need to create a <a href="https://console.cloud.google.com/projectcreate">New project</a> 
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/cf3872e9-096a-4e57-b840-266b1dc24a22)
Step 2: You will be getting this:
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/07e4ddae-2bb2-4d6a-a304-0b46186052c2)
Step 3: Click on the 3 lines(ham-burger) on left side --> Select Cloud Storage --> Buckets.
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/299ed9a3-3ff8-4517-a654-b0db7d6a7185)
Step 4: Click on Create.
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/1b32e9da-2abf-4b05-ad1b-3db729f17b31)
Step 5.1: Give Name to your bucket.
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/3b4bf305-5d91-43c5-acd5-5324f027c529)
Step 5.2 : Choose where to store your data
            Location: us-central1 (Iowa)
            Location type: Region
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/fe6c1020-e02f-4f94-b509-b964ed374c92)
Step 5.3 : Click Create.
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/312dfc09-813d-4d63-8e11-9a02cb4c3492)
Step 5.4 : Public access will be prevented
This bucket is set to prevent exposure of its data on the public internet.
Keep this setting enabled unless you have a use case that requires public access (such as static website hosting). You can change it now or later. Learn more 
select : "Enforce public access prevention on this bucket" and click - "Confirm".
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/5d649552-498e-4210-a04e-960e3bc42a12)
Step 5.6 : Check your Bucket(Upload a file.
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/7ce9397a-ae20-42a9-bfa1-da21d86bd9ed)
Step 5.7 : It's Working.If not working <a href= "https://cloud.google.com/storage/docs/creating-buckets">Google guide here</a>
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/50b0a5d8-abee-44ea-baa2-bf664298678b)

<h1>For Key</h1>
Step 1:Click on the 3 lines(ham-burger) on left side --> I AM & Admin --> Service Accounts
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/1a12ce80-1b05-4e3e-8a7d-5427b69e98fe)
Step 2: Click on "Create Service Account".
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/987b4941-8d8e-4403-b5c7-fca5a917036a)
Step 3 : Service Account Name. --> Click on "Create and Continue".
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/1d698b31-e799-4758-9fab-4a99ab080e75)
Step 4: 
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/c056aa9c-179e-47b4-a733-71df54a05f49)
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/0afb5ca0-144e-4e46-b933-4198833e6434)

Note - As we are just making a demo, we are making the uploader as a owner else we need to give only the rights needed to them.(Based on their role) <a href="https://cloud.google.com/iam/docs/overview">IAM overview</a>
Optional Step - Grant users access to this service account.
If you want to add someone's Email ID you can do here else leave it blank.
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/fce28bac-abba-4d75-89af-38370da517eb)
Click Done.
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/c18a32f9-0ff8-4d6a-ac9c-10dc7f3adb8b)
Now Get the keys.
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/cd2a7afa-b594-4f52-8e39-971424a8cf3b)
Click on Add key --> Create new key.
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/1f7ba849-a4ce-4b86-bf0e-c34489333e4c)
Select .JSON --> Cleck "Create". (The key will be Downloaded auto matically-Keep it safe as it contains important data.)
![image](https://github.com/suragsp/Microservice-GCP/assets/104720115/5ec59b69-b440-4ce9-ae32-aec820140457)













 

