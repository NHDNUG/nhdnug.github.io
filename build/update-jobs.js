const requestPromise = require("request-promise");
const cheerio = require("cheerio");
const nodeUrl = require("url");
var yaml = require('write-yaml');

console.log("Starting Update Improving Jobs...");

const options = {
    uri: "http://improving.com/careers",
    transform: function(body) {
        return cheerio.load(body);
    }
};

const desiredLocation = "Houston";
const sponsor = "Improving";

const jobs = [];

requestPromise(options).then(($) => {
    $(".m-searchable-table tbody tr").each(function(jobIndex, element) {
        const job = {
            sponsor
        };
        
        $(this).find("td").each((function(cellIndex, element) {
            const text = $(this).text();            
            switch(cellIndex) {
                case 0:
                    const link = nodeUrl.resolve("http://improving.com", $(this).find("a").attr("href"));
                    job.title = text;
                    job.link = link;
                    break;
                case 1:
                    job.category = text;
                    break;
                case 2:
                    job.type = text;
                    break;
                case 3:
                    job.location = text;
                    break;
            }
        }));

        if (job.location.includes(desiredLocation)) {
            jobs.push(job);
        }        
    });    

    yaml("./_data/sponsor-jobs.yml", jobs, function(err) {
        if (err) {
            console.log(err);
        } else {
            console.log("Finished Update Improving Jobs.");    
        }
        
    });


}).catch((err) => {
    console.error(err);
})