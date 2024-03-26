# Water-Wise-Demo
The purpose of this project is to demo the IF Water-Wise plugin

Check correct if-plugin is linked with this command:
```
npm ls -g --depth=0 --link=true
```

## Installation/Build Instructions

Install IF framework, official, and unofficial plugins as described in the docs

To run the manifest file:
```
npx ie --manifest ../water-wise-demo/manifests/water-wise-demo.yml --output computed#carbon
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


