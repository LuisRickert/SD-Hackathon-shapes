import sys
import json
import pathlib
from datetime import datetime as dt

def create_signable_sd(subject: json) -> json:
  return {
        "@id": "http://example.edu/verifiablePresentation/self-description1",
        "type": ["VerifiablePresentation"],
        "@context": ["https://www.w3.org/2018/credentials/v1"],
        "verifiableCredential": {
            "issuanceDate": str(dt.now()),
            "credentialSubject": subject,
            "@type": ["VerifiableCredential"],
            "@id": "https://www.example.org/SoftwareOffering.json",
            "@context": ["https://www.w3.org/2018/credentials/v1"],
            "issuer": "https://gaiax.de"
        }
    }

if __name__ == "__main__":
    path_to_file = pathlib.Path(sys.argv[1])
    
    if path_to_file.is_dir():
       files = [file for file in path_to_file.iterdir() if file.is_file() and file.name.endswith("json")]
    elif path_to_file.is_file() and path_to_file.name.endswith("json"):
       files = [path_to_file]
    else:
       raise ValueError("path to files or file")
    
    for file in files:       
       with open(file,'r') as read_file:
          sd = json.load(read_file)

       
       signable_sd = create_signable_sd(sd)       
       new_name=pathlib.Path("./signable_" + file.name)
       new_name.touch(exist_ok=True)
       with open(new_name,"w") as file:
          json.dump(create_signable_sd(sd),file)