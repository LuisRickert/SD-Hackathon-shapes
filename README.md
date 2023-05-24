# SD-Hackathon-shapes

This repository is used to track the progress of the SelfDescription Team during the Gaia-X GXFS Hackathon (22.05-23.05.2023).
In this repository we want to collect our learnings and provide guidance to follow our steps.

## Shapes

In the directory `shapes` there are some shapes we defiend for the Hackathon. They are derived from the previouse [Hackahton in Berlin](https://gitlab.com/gaia-x/data-infrastructure-federation-services/gxfs-hackathon/gxfs-workshop-drinks-usecase). We used these shapes to generate Self Descriptions.

For the Hackathon we developed the following roles that need their own self descriptions.

- Dispatcher:
  Description of a member that uses the Vehicle Position Service.

- Supervisor:
  Federation member that supervises the Vehicle that provides the data for the VehiclePositionService.
- VehiclePositionService:
  Description of the Vehicle Position Service.

- Service Owner:
  Descprition of a federation member that provides the service.

## Self Descriptions

We used the [Self-Description Wizard](https://gitlab.com/gaia-x/data-infrastructure-federation-services/self-description-tooling/sd-creation-wizard) to create the Self-Descriptions based on the defined shapes above. The resulting Self-Descriptions had to be transformed such that the signer tool accepts those. This transformation was done with a script that we created located at `./scripts/make_signable.py`.

We used [this](https://gitlab.com/gaia-x/data-infrastructure-federation-services/cat/fc-tools/signer) signer to sign the self-description.

### Self-Description Wizard

We run the Self-Description Wizard on our local machine with the provided docker compose file located in the Self-Description-Wizard-Frontend repo. We had to build the images for the frontend and api. To do so run `mvn clean install` inside the root of the api repository and `yarn build` within the implementation dir.

Note:

- use the tag option `"-t"` for both builds and modify the docker-compose file to use those images.

### Self-Description Signer

The singer is one java file. The script searches in the resource folder for a self-description named `sd.jsonld`. To use this signer you have to set the target location of the script within the main.java .

## Steps

1. Start the Self-Description Wizard navigate to upload shape and add each shape an fill the empty fields.
2. run the `make_signable.py`script by passing the created Self-Descriptions
3. Sign each Self-Description
4. add the .rdf file to the FC together with the shapes

## Result

- In the postman dir you find a postman collection to interact with the federated catalog
- In the example dir you find the generated Self Descriptions usinged aswell as unsigned.
- as for now the federated catalogue does **not** accept these Self-Descriptions due to malformed credential subject.
  - we assume this is depening on the super class LegalPerson
  - we assume this, because the during the Berlin-Hackathon the used super class was "Service Offering". In this context the Self-Descriptions created and signed the same way were accepted.
