# Water-Wise-Demo
The purpose of this project is to demo the IF Water-Wise plugin

Check correct if-plugin is linked with this command:
```
npm ls -g --depth=0 --link=true
```

Make sure to build changes in the linked `if-plugins` repo:
```
npm run build
```

Run this after making updates to the local plugin
```
npm link @grnsft/if-plugins
```

## Installation/Build Instructions

Install IF framework, official, and unofficial plugins as described in the docs

To run the manifest file:
```
npx ie --manifest ../water-wise-demo/manifests/water-wise-demo.yml --output computed#water
```

## Scenario

We are deploying an ML application with most traffic in North Africa.  We need to decide between which region to deploy the app.
How do we make this decision?

* europe versus middle east vs us west
* azure vs aws vs gcp

Application specs:
-database instance
-serverless app
-docker deployed
- ML app


## References
* https://www.thoughtworks.com/en-us/insights/articles/cloud-native-sustainability
* https://demo.cloudcarbonfootprint.org/
* https://azuretracks.com/2021/04/current-azure-region-names-reference/
* https://medium.com/teads-engineering/building-an-aws-ec2-carbon-emissions-dataset-3f0fd76c98ac
* https://www.cloudcarbonfootprint.org/docs/embodied-emissions
* https://dgtlinfra.com/data-center-water-usage/#:~:text=Water%20Usage%20Effectiveness%20(WUE)%20is,kilowatt%2Dhour%20of%20electricity%20consumed


## Notes
Industry average WUE is 1.8 liters / kWH

Cooling methods:
* direct evaporative cooling (preferred) = hot air is pushed through water-soaked cooling pads, reducing air's temp
* free-air cooling = when conditions within safe operating ranges, deactivates evaporative cooling system
* adiabatic cooling = uses outside air when temps < 85 deg

Strategies for Water Positive
* Improving water use efficiency across its operations
* Using sustainable water sources (e.g., recycled water)
* Returning water for community reuse
* Supporting water replenishment projects for communities and the environment

Data center conditions:
* Recommended temperature in data centers maintained within range 
of 18°C to 27°C (64°F to 81°F)
* humidity levels for data centers should fall within the range of 40% to 60%


### AWS
20 data centers use recycled water = Virginia, California, Oregon, United Kingdowm, Spain, Brazil, South Africa, India, Indonesia, Singapore, Australia

Global WUE is 0.19 L/KWh


### Microsoft
FY22 withdrew 10.7 million cubic meters
discharges 4.3 million cubic meters

WUE per region
https://azure.microsoft.com/en-us/blog/how-microsoft-measures-datacenter-water-and-energy-use-to-improve-azure-cloud-sustainability/

https://datacenters.microsoft.com/globe/fact-sheets/

### Google
withdrew 6.6 billion gallons
discharged 1.4 billion gallons
List of water withdrawl per data center

### Meta
withdrew 956 million gallons
dishcarge of 293 million gallons
Average WUE = 0.2 L/kWhr
List of water withdrawl per data center


### Apple
withdrew 1.53 billion gallons and discharged 679 million gallons (inclues retail stores, distribution centers, and offices)



## Contributing
* To contribute to the repository use the following:
```commandline
git clone <ENTER SSH HERE>
cd reponame
git lfs install
git checkout -b feature/feature_name
git add <files>
git commit -m "Add my feature"
git push origin feature/feature_name
```


