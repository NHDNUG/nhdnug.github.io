<Query Kind="Statements">
  <Reference>&lt;RuntimeDirectory&gt;\System.Web.dll</Reference>
</Query>

//Util.WriteCsv(Nh_Speakers, "C:\\temp\\speakers.csv")
var rowsToExport = Nh_Speakers
	// Speaker 6 is TBD
	// Speaker 9 and 45 was two speakers. Not sure how to handle that.
	// Speaker 39 is "Various"
	.Where(x => x.SpeakerID != 6 
		&& x.SpeakerID!=9
		&& x.SpeakerID != 39
		&& x.SpeakerID != 45
		)
	.ToList()
	.Select(x => new
	{
		x.SpeakerID,
		x.NameFirst,
		x.NameLast,
		FullName = $"{x.NameFirst} {x.NameLast}",
        x.CompanyName,
		x.Bio,
		x.URL,
		x.EmailAddress1,
		x.PhoneNumber1,
		x.PhoneNumber2,
		x.Twitter,
	})
	.Take(45);
//rowsToExport.Dump();
var foo = new XElement(
	"speakers", rowsToExport.Select(x =>
		new XElement("speaker", new XAttribute("id", x.SpeakerID),
			new XElement("name", x.FullName),
			new XElement("company", x.CompanyName),
			new XElement("bio", x.Bio),
			new XElement("url", x.URL),
			new XElement("email", x.EmailAddress1),
			new XElement("twitter", x.Twitter)
        )
	)
);
foo.Dump();
//Util.WriteCsv(rowsToExport, "c:\\temp\\speakers.csv");