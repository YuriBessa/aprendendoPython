#Buscando dados de uma API de noticias

import requests


def get_news(topic, from_date, to_date, language='en', api_key='890603a55bfa47048e4490069ebee18c'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
    r=requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n'{article['title']},'\nDESCRIPTION\n', {article['description']}")
    return results

print(get_news(topic='space', from_date='2024-12-02', to_date='2024-12-03'))

'''
["TITLE\n'Space station video shows ‘cosmic fireflies’ high above Earth, '\nDESCRIPTION\n', Space station astronaut Don Pettit has captured footage of what he describes as 
'cosmic fireflies.'", "TITLE\n'Day 3 of the 2024 Space Telescope Advent Calendar, '\nDESCRIPTION\n', @TheAtlPhoto is sharing a new image from a space telescope every day until December 25.\r\n\r\nThis photo from Hubble shows the distinctive wavy lanes of dust of lenticular galaxy NGC 4753:", "TITLE\n'Student aims to grow Canada's space program with Polytechnique White Rose scholarship, '\nDESCRIPTION\n', At 23 years old, Makenna Kuzyk is the first woman and second civilian to be admitted to the International Test Pilots School in London, Ont., where she plans...", "TITLE\n'Inside the Hubble Space Telescope's 23-year-long look at a beautiful blue galaxy, '\nDESCRIPTION\n', None", 
"TITLE\n'Never Use a Space Heater in These 9 Danger Zones, '\nDESCRIPTION\n', Space heaters come with serious fire hazards: Here's what you need to know when using one.", "TITLE\n'Palmes's Copenhagen Hybrid Space Merges Tennis Influences With an Industrial Aesthetic, '\nDESCRIPTION\n', Danish menswear label Palmes has unveiled a brand new location in Copenhagen’s vibrant Carlsberg Byen district. Dubbed, Palmes\xa0Center\xa0Court, the new-opened hybrid space spans 135 square meters, comprising an exhibition space, studio while also serving the bra…", "TITLE\n'Europe’s Proba-3 satellites will launch early Dec. 4 to create artificial eclipses in space. Watch the liftoff live, '\nDESCRIPTION\n', An Indian PSLV rocket will launch Europe's Proba-3 precision formation-flying mission to orbit early Wednesday (Dec. 4), and you can watch the action live.", "TITLE\n'Fruit flies in space! Chinese astronauts show off experiment on Tiangong space station (video), '\nDESCRIPTION\n', China's Shenzhou 19 astronauts have some winged companions to oversee aboard the country's Tiangong space station — fruit flies, which arrived on a cargo ship on Nov. 15.", "TITLE\n'Inside the Hubble Space Telescope's 23-year-long look at a beautiful blue galaxy, '\nDESCRIPTION\n', NASA's Hubble Space Telescope explores the evolution of spiral galaxy UGC 10043 through images taken 23 years 
apart, in 2000 and 2023.", "TITLE\n'This YouTuber is Offering You the Chance to Take a Selfie in Space, '\nDESCRIPTION\n', If you have ever wanted to grab a selfie from space which, let's face it, who wouldn't? Then a YouTuber is offering an opportunity to do so, kind of.\n[Read More]", "TITLE\n'Coastal revelations from space: New satellite tech maps sandy beaches, '\nDESCRIPTION\n', Scientists have developed a method to map sandy beach intertidal zones with unprecedented accuracy using satellite data. This innovative approach allows for precise measurements of coastlines that are constantly shaped by tides and waves, providing crucial in…", "TITLE\n'A New Reconfigurable Structure Could Be Used to Make Space Habitats, '\nDESCRIPTION\n', Even some fields that seem fully settled will occasionally have breakthrough ideas that have reverberated impacts on the rest of the fields of science and technology. Mechanics is one of those relatively settled fields – it is primarily understood at the macr…", "TITLE\n'T-Mobile Tuesdays Offers The Chance To “Take A Selfie” From Space, '\nDESCRIPTION\n', Here's your best chance to take a selfie from space... Sort of.", "TITLE\n'Bathroom of the Week: Terrazzo Dazzles in a 68-Square-Foot Space (8 photos), '\nDESCRIPTION\n', A designer’s fresh take on midcentury modern style creates a functional bathroom that will grow with two little girls", "TITLE\n'Bathroom of the Week: Terrazzo Dazzles in a Functional Space (8 photos), '\nDESCRIPTION\n', This Southern California couple’s two toddler daughters shared a bathroom that was overflowing with baby items...", "TITLE\n'Wall Street Journal Tries “Recovery Finally Underway” Office Space Patter as Securitized Office Mortgage Delinquencies Hit a New Post-Crisis High of 10.4%, '\nDESCRIPTION\n', The Journal gets egg on its face for trying to call a bottom in the office space market even as delinquencies were accelerating", "TITLE\n'Space firms plot new European satellite venture to take on Starlink, '\nDESCRIPTION\n', Europe's Airbus , Thales and Leonardo are exploring plans to set up a new joint space company as they look to compete with Elon Musk's Starlink.", "TITLE\n'Astronomers Have Pinpointed the Origin of Mysterious Repeating Radio Bursts From Space, '\nDESCRIPTION\n', Slowly repeating bursts of intense radio waves from space have puzzled astronomers since they were discovered in 2022. In new research, my colleagues and I have for the first time tracked one of these pulsating signals back to its source: a common kind of lig…", "TITLE\n'Earth from space: Crimea's 'putrid sea' creates beautiful rainbow of color but smells like rotten eggs, '\nDESCRIPTION\n', A 2014 satellite photo of the Sivash region shows off the kaleidoscopic colors of a series of shallow, hypersaline lagoons — each filled with a different kind of algae.", "TITLE\n'James Webb Space Telescope smashes its own record to find the 
earliest galaxies that ever existed, '\nDESCRIPTION\n', The James Webb Space Telescope has spotted five galaxy candidates dating to just 200 million years after the Big Bang, making them the earliest ever detected. And there could be many more.", "TITLE\n'New Report Highlights Serious Concerns About The Safety Of The International Space Station And Whether It Will Be Able To Last Until 2030, '\nDESCRIPTION\n', I can't wait until there are many space stations in operation.", "TITLE\n'Photos Show Laika, the First Dog in Space?, '\nDESCRIPTION\n', Black-and-white photographs authentically show Laika, a Moscow mutt sent to space aboard Sputnik 2 in 1957.", "TITLE\n'BMW iX3 Neue Klasse SUV: Spy Photos Reveal Frunk Space and Production Lights, '\nDESCRIPTION\n', BMW’s upcoming iX3 Neue Klasse SUV (codename NA5) is inching closer to its big debut, and new spy shots give us the clearest look yet at this fully electric model. Spotted during testing in Hungary,...\nFirst published by https://www.bmwblog.com", "TITLE\n'European Space Agency's Proba-3 mission to create artificial solar eclipses in space, '\nDESCRIPTION\n', The European Space Agency (ESA) is set to launch a pioneering mission that 
will create artificial solar eclipses in space. The Proba-3 mission, scheduled for liftoff on Wednesday, December 4, 2024, from India's Satish Dhawan Space Center, aims to 
transform so…", "TITLE\n'[Removed], '\nDESCRIPTION\n', [Removed]", "TITLE\n'Toronto has too much garbage and not enough space for it, '\nDESCRIPTION\n', Toronto is in the process of formulating\xa0a new waste strategy\xa0to address the city's trashy elephant in the room:\xa0the fact that\xa0the\xa0Green Lane Landfill,\xa0the site some 200 km 
away that\xa0receives most of our\xa0waste, is\xa0currently on track to\xa0overflow\xa0in about a dec…", "TITLE\n'Nomura has space to cut a further $187 million in costs, CEO says, '\nDESCRIPTION\n', None", "TITLE\n'Rocket Lab Soars 530%: Defense Deals and Space Milestones Propel Stock to New Heights, '\nDESCRIPTION\n', None", 'TITLE\n\'Space firms plot new European satellite venture to take on Starlink, \'\nDESCRIPTION\n\', Europe\'s Airbus, Thales and Leonardo are exploring plans to set up a new joint space company as they look to compete with Elon Musk\'s Starlink.  "Project...', "TITLE\n'Proozy - Canada Weather Gear Men's Supreme Soft Space Dye 1/4 Zip Pullover $26.99, '\nDESCRIPTION\n', Use the Proozy promo code at checkout to B1G2 Free!!\xa0 Plus shipping is free too!!", "TITLE\n'Review: STAR WARS: SKELETON CREW Takes Fans on an Amblin-Style 
Space Odyssey, '\nDESCRIPTION\n', As a lifelong Star Wars fan and someone who grew up in the golden era of ‘80s adventure films, Star Wars: Skeleton Crew on Disney+ feels like a vibrant love letter to the stories I thought were awesome as a kid. It’s a delightful mix of sci-fi fantasy and nos…", "TITLE\n'Milwaukee Interstate Removal Would Create Space for Thousands of New Housing Units, '\nDESCRIPTION\n', Milwaukee Interstate Removal Would Create Space for Thousands of New Housing Units\nDiana Ionescu\nMon, 12/02/2024 - 06:00\n\n\n \n Primary Image\r\n\n \n\n\n\r\n\n \n\n\n \n Primary Image Caption\r\n\n Interstate 794 in Milwaukee, Wisconsin.\r\n\n \n\n\n A new report outlines the poten…", "TITLE\n'Create Epic Space Scenes With StarGen [$], '\nDESCRIPTION\n', Create volumetric starfields and nebulae with this new add-on by Stefan Kotuziak. Do you 
want to create detailed starfields and nebulae for your next space epic quickly and easily? Do you want complete control over those starfields and nebulae? Do you want a …", "TITLE\n'Astronomers have pinpointed the origin of mysterious repeating radio bursts from space, '\nDESCRIPTION\n', Slowly repeating bursts of intense radio waves from space have puzzled astronomers since they were discovered in 2022. In new research, we have for the first time tracked one of these pulsating signals back to its source: a common kind of lightweight star cal…", "TITLE\n'NEW RULES for Space Mountain that Disney Adults Are Begging For, '\nDESCRIPTION\n', Don't ride Space Mountain without these rules!\nThe post NEW RULES for Space Mountain that Disney Adults Are Begging For first appeared on the disney food blog.", "TITLE\n'A Prolific Italian Restaurateur Is Serving Tuscan Classics in an Iconic Beverly Grove Space, '\nDESCRIPTION\n', Florence Osteria & Piano Bar opens in the former Nic’s on Beverly on December 5", "TITLE\n'Footprints 
in Kenya Suggest Ancient Human Relatives Shared Space, '\nDESCRIPTION\n', PITTSBURGH, PENNSYLVANIA—According to a Science News report, Kevin G. Hatala of Chatham University and his […]\nThe post Footprints in Kenya Suggest Ancient Human Relatives Shared Space appeared first on Archaeology Magazine.", "TITLE\n'‘Skeleton Crew’ Finds a New ‘Star Wars’ Show Lost in Space, '\nDESCRIPTION\n', A franchise without a clear direction makes another uneven TV show. Continue reading…", "TITLE\n'China advances space ambitions with next-gen Beidou navigation system, '\nDESCRIPTION\n', China's satellite navigation ambitions are accelerating, with plans for a next-generation BeiDou system taking 
shape amid growing commercial adoption of the technology. The expansion comes as Chinese tech giants leverage satellite capabilities in their latest…", "TITLE\n'Poland-Taiwan space partnership takes flight at TASTI 2024, '\nDESCRIPTION\n', Poland marked a significant diplomatic milestone at the TASTI Expo 2024 with the first-ever Polish Space Agency delegation to Taiwan, led by Michal Wiercinski, Vice President of POLSA. The visit culminated in a landmark memorandum of understanding (MOU) betwe…", "TITLE\n'Avoid Giant Candies and Baubles During Christmas in 2 Minutes in Space!, '\nDESCRIPTION\n', Taking a hilariously chaotic turn!\nThe post Avoid Giant Candies and Baubles During 
Christmas in 2 Minutes in Space! appeared first on Droid Gamers.", "TITLE\n'Reclaim cabinet space with Joseph Joseph’s 6-piece nested mixing bowl set at $18 (Reg. $34), '\nDESCRIPTION\n', Joseph Joseph 6-piece Nested Mixing Bowl Set\n\n\n\nBuy for $18 (Reg. $34)\n\n\n\n\n\n\n\n\r\n\n\r\n\n\n\n\nWhat we love\r\n\n\n\n\nOutfitted with three mixing bowls, two preparation bowls, and a strainer, you’re looking at a set with plenty of options to suit a majority of your kitche…", "TITLE\n'Nomura has space to cut a further $187 million in costs, CEO says, '\nDESCRIPTION\n', TOKYO : Japan's largest securities firm Nomura Holdings has room to cut costs by a further 28 billion yen ($187 million) in the short- to medium-term, Chief Executive Officer Kentaro Okuda told an investor summit on Tuesday.The efforts mark the latest in Nomu…", 'TITLE\n\'Space firms plot new European satellite venture to take on Starlink, \'\nDESCRIPTION\n\', PARIS/ROME : Europe\'s Airbus, Thales and Leonardo are exploring plans to set up a new joint space company as they look to compete with Elon Musk\'s Starlink."Project Bromo", named after an Indonesian volcano, envisages a standalone European satellite champion …', 'TITLE\n\'A lot of Sony\'s leadership didn\'t take the PS1 seriously at first with Nintendo and Sega dominating the console space: "They didn\'t want to be associated with it", \'\nDESCRIPTION\n\', The PlayStation 1 was seen by some as a "fool\'s errand"', "TITLE\n'New planet in Kepler-51 system discovered using James Webb Space Telescope, '\nDESCRIPTION\n', An unusual planetary system with three known ultra-low density 'super-puff' planets has at least one more planet, according to new observations.", "TITLE\n'Europe weighs its future in space, '\nDESCRIPTION\n', The United States is not the only country wondering what the next administration will do in space policy. Jeff Foust reports that, in Europe, the prospect of changes in US-European space cooperation is fueling calls for the continent to invest more in space c…", "TITLE\n'Tollways in space: from sci-fi to saving grace, '\nDESCRIPTION\n', The space industry has struggled to develop financial models for funding removal of orbital debris even as the problem of debris worsens. Polina Shtern offers an approach that treats orbits as tollways to pay for debris cleanup.", "TITLE\n'Donald Trump's approach to US space policy could throw up some surprises, especially with Elon Musk on board, '\nDESCRIPTION\n', The impacts of the incoming Trump Administration on space policy are still to be determined nearly a month after the election. Bleddyn Bowen and P.J. Blount discuss what could change and what might remain the same in the next administration.", 'TITLE\n\'Woman Measures Furniture Space With Hands, the Results Speak for Themselves, \'\nDESCRIPTION\n\', Social-media users were in stitches over the miscalculation in the viral clip, with one noting their "claustrophobia being activated."', "TITLE\n'Astronomers have pinpointed the origin of mysterious repeating radio bursts from space, '\nDESCRIPTION\n', By searching sparsely populated regions of the galaxy, astronomers have for the first time found the source of a kind of signal that has puzzled them for years.", "TITLE\n'Elevate Your Dining Space: Choosing Kitchen Chairs That Combine Style And Functionality, '\nDESCRIPTION\n', There’s nothing like a dining room that feels chic yet inviting. And, whether you’re entertaining a crowd or just sitting down with your nearest and dearest, kitchen chairs influence the mood of the room. They’re more than places to park your, well, seat. The…", 'TITLE\n\'Canada Weather Gear Men\'s Supreme Soft Space Dye 1/4 Zip Pullover: 3 for $27 + free shipping, \'\nDESCRIPTION\n\', Add three to your cart and apply coupon code "PZY2CP-FS" to drop the total and dodge the shipping fee. That\'s just $9 each. Buy Now at Proozy', "TITLE\n''I wasn't in a good head space': Gregg Wallace apologises over 'women of a certain age' video, '\nDESCRIPTION\n', MasterChef presenter Gregg Wallace has apologised for his response to claims he made sexual comments towards staff and celebrity guests on a range of programmes over 17 years.", "TITLE\n'Decorating With Brown is Not Outdated: How to Use it in Your Space, '\nDESCRIPTION\n', With the rise of more colorful earthy interiors, the color brown is back as a rich and nuanced choice for interiors and exteriors alike. While decorating with brown might not feel like an obvious choice, using brown can bring warmth, sophistication, and groun…", "TITLE\n'Hurry, there’s a Double Discount on this Bosch Space-Saving 12″ Miter Saw!, 
'\nDESCRIPTION\n', Enjoy stacked savings on this popular space-saving miter saw!", "TITLE\n'  Berlin weekend: sleep in a space pod in the heart of the city  , '\nDESCRIPTION\n', Pirates, Berlin is one of the most fun places to spend a weekend in Europe, but it can be expensive. That's why we were chuffed to spot this cool and quirky space themed hostel, right in the centre of Berlin. \u200d From £120, you'll get flights and a two night …", "TITLE\n'Disney Fans Beg for Space Mountain to Change After 49 Years, '\nDESCRIPTION\n', Space Mountain at Disney World is one of the most iconic attractions in Magic Kingdom, drawing millions of guests each year. Opened in 1975, this classic indoor roller coaster was Disney’s first thrill ride and remains a fan favorite for its unique concept an…", "TITLE\n'Starship to Shipyards: How Space Policy Could Save U.S. Maritime Power, '\nDESCRIPTION\n', Can lessons learned in space help us revitalize america’s maritime economy? By\xa0Bruce Kimbrell\xa0(Policy Op-Ed) On the 249th anniversary of the U.S. Navy’s founding, America celebrated an unexpected milestone—not at sea,...", "TITLE\n'Searching the Chemical Space of Hetero-Atom Bridged Norbornadienes, '\nDESCRIPTION\n', Phys. Chem. Chem. Phys., 2024, Accepted ManuscriptDOI: 10.1039/D4CP04179H, Paper Open Access &nbsp This article is licensed under a Creative Commons Attribution 3.0 Unported Licence.Nils Oberhof, Andreas Erbs Hillers-Bendtsen, Oscar Berlin Obel, Karoline Schj…", "TITLE\n'James Webb Space Telescope smashes its own record to find the earliest galaxies that ever existed, '\nDESCRIPTION\n', None", "TITLE\n'Quick recovery from 2024: BJP has again acquired more political space for manoeuvrability & comfort, '\nDESCRIPTION\n', The BJP is regaining political strength after election successes in Maharashtra and Haryana. These victories have bolstered the party's stance on key issues like the Agniveer scheme and caste census. The results may provide the government confidence in its go…", "TITLE\n'Storm Collectibles Cobra the Space Pirate Figure Available For Pre-Order, '\nDESCRIPTION\n', Storm Collectibles Cobra the Space Pirate Figure Available For Pre-Order", "TITLE\n'We Did the Math: Here's How Much a Space Heater Can Lower Your Heating Bill, '\nDESCRIPTION\n', Depending on where you live and how you heat your home, adding a space heater could be a big money-saver this winter.", "TITLE\n'Student aims to grow Canada's space program with Polytechnique White Rose scholarship, '\nDESCRIPTION\n', A ceremony was held Monday morning to honour the 10th recipient of Polytechnique's Order of the White Rose, a $50,000 bursary created in memory of the 14 women murdered at Polytechnique in 1989.", "TITLE\n'NASA’s Nancy Grace 
Roman Space Telescope Nears Completion with New Assembly, '\nDESCRIPTION\n', NASA's Nancy Grace Roman Space Telescope has taken a major step forward with the delivery of its Optical Telescope Assembly to Goddard Space Flight Center. Designed to enhance infrared observations of the cosmos, the assembly includes a primary mirror and sup…", "TITLE\n'ISRO Chief S Somanath Supports Elon Musk’s Model to Boost Space Economy, '\nDESCRIPTION\n', ISRO Chairman S Somanath stressed the importance of private-sector involvement in advancing India’s space activities. Speaking at Huddle Global 2024, he endorsed Elon Musk’s sustainable model for space exploration and highlighted the need to grow 
India’s sate…", "TITLE\n'Fruit Fly Experiment on Tiangong Space Station Explores Effects of Microgravity, '\nDESCRIPTION\n', Chinese astronauts are studying fruit flies aboard the Tiangong space station to understand how microgravity and sub-magnetic fields affect living organisms. The research focuses on biological rhythms, molecular mechanisms, and movement patterns, with samples…", "TITLE\n'Space Workforce for Tomorrow Announces National Space Day STEM Competition for Middle School Students, '\nDESCRIPTION\n', Empowering Middle School Innovators to Develop Solutions for Space Debris and Shape the Future of Space Sustainability Empowering Middle School Innovators to Develop Solutions for Space Debris and Shape the Future of Space Sustainability", "TITLE\n'Why Investments In Space Could Skyrocket, '\nDESCRIPTION\n', The space industry was once the exclusive domain of the government. Agencies like NASA in the US, Roscosmos in Russia and the China National Space Administration have long dominated space exploration and the industry surrounding it, making private sector inve…", "TITLE\n'Space Battery Technology Market Size\xa0Projected to Reach $6.56 Billion by 2032 Playing a Critical Role in Space Exploration, '\nDESCRIPTION\n', PALM BEACH, Fla., Dec. 03, 2024 (GLOBE NEWSWIRE) -- FN Media Group News Commentary - The space battery market is expanding swiftly as improved batteries meet the high-demand needs of space missions with superior energy density, safety, and lightweight perform…", "TITLE\n'Astrology Meets Space: Planets That Radiate Peace and Calm, '\nDESCRIPTION\n', Certain planets in astrology are believed to promote calm and harmony. The Moon, Venus, Jupiter, Neptune, and Saturn each 
play roles in fostering emotional balance, joy in relationships, optimism, relaxation, and long-term peace through structure. Their energ…", "TITLE\n'Japan takes first step toward space-based solar power supply, '\nDESCRIPTION\n', TOKYO -- A team of Japanese researchers are launching an experiment Wednesday to test technology that would collect solar energy in space and transmit power to Earth.\nJapan Space Systems (JSS) will operate aircraft equipped with solar panels flying 5-to-7 kil…", "TITLE\n'Enron announces plans to relaunch and teases entry into the crypto space, '\nDESCRIPTION\n', Enron announces its surprising comeback after its 2001 bankruptcy and fraud scandal, unveiling plans for energy and blockchain innovation.\nThe post Enron announces plans to relaunch and teases entry into the crypto space appeared first on Crypto Briefing.", "TITLE\n'Nomura has space to cut a further $187 mln in costs, CEO says, '\nDESCRIPTION\n', Japan's largest securities firm Nomura Holdings has room to cut costs by a further 28 billion yen ($187 million) in the short- to medium-term, Chief Executive Officer Kentaro Okuda told an investor summit on Tuesday.", "TITLE\n'Space Startups Get Government Contracts as SpaceX Explores Share Sale Valued at $350 Billion, '\nDESCRIPTION\n', The commercial space industry has had a rocket lit under it recently, as the government 
changes how it awards contracts, looking closely at new innovators.", "TITLE\n'Townsquare Capital LLC Raises Position in Extra Space Storage Inc. (NYSE:EXR), '\nDESCRIPTION\n', Townsquare Capital LLC lifted its position in Extra Space Storage Inc. (NYSE:EXR – Free Report) by 30.9% during the 3rd quarter, HoldingsChannel reports. The institutional investor owned 8,267 shares of the real estate investment trust’s stock after acquiring…", "TITLE\n'California’s space cadets: Dreams of asteroid mining, orbital manufacturing and much more, '\nDESCRIPTION\n', Dreams of asteroid mining, orbital manufacturing and much more\nIdeas for making money in orbit that seemed mad in the 1960s now 
look sane\nCalling A company SpinLaunch in an industry where the first part of that name is a way of life might seem a hostage to fo…", "TITLE\n'Tech firm signs huge Menlo 
Park office deal, enough space for thousands, '\nDESCRIPTION\n', MENLO PARK — A tech company has signed a mammoth office deal in the South Bay, a transaction that is poised to provide a huge boost for the region’s economy, job market and commercial real estate sector.\nSnowflake has subleased 773,000 square feet in Menlo Pa…", "TITLE\n'Space 
regulator INSPACe announces Hyderabad company as India’s first private satellite operator, '\nDESCRIPTION\n', Hyderabad-based Ananth Technologies Ltd (ATL) is set to become India's first private satellite operator, marking a significant milestone in the Indian space sector. IN-SPACe has designated ATL to manage a multi-beam Ka band communication satellite project, in…", "TITLE\n'I made my space in this industry without a godfather, says Nikki Tamboli, '\nDESCRIPTION\n', Nikki Tamboli, known for Bigg Boss 14, addresses her close friendship with Arbaz Patel from Bigg Boss Marathi, denying any dating rumors. She shares she isn't ready for marriage now but is content with her current relationships. Nikki reveals upcoming project…", "TITLE\n'Freedom Investment Management Inc. Sells 151 Shares of Extra Space Storage Inc. (NYSE:EXR), '\nDESCRIPTION\n', Freedom Investment Management Inc. decreased its stake in shares of Extra Space Storage Inc. (NYSE:EXR – Free Report) by 11.1% in the 3rd quarter, according to its most recent 13F filing with the SEC. The firm owned 1,206 shares of the real estate investment …", 'TITLE\n\'Woman Measures Furniture Space With Hands, the Results Speak for Themselves, \'\nDESCRIPTION\n\', A video about the awkward placement of a coat closet in a home has gone viral on TikTok.\nThe clip begins with a note saying, "My wife\'s measuring skills," as a man is shown standing between a wall and a closet in a corridor space just outside a bathroom.\nA vo…', "TITLE\n'India must become data self-reliant: IN-SPACe chief Pawan Goenka, '\nDESCRIPTION\n', HYDERABAD/NEW DELHI, Dec 2: Space sector regulator IN-SPACe’s chairman Pawan Goenka on Monday said India faces significant gaps in 
meeting all its space data needs and remains heavily reliant on foreign providers. Addressing the GeoSmart India 2024 conference…", "TITLE\n'Nomura has space to cut a further $187 million in costs, CEO says, '\nDESCRIPTION\n', Nomura has space to cut a further $187 million in costs, CEO says", "TITLE\n'Space firms plot new European satellite 
venture to take on Starlink, '\nDESCRIPTION\n', Space firms plot new European satellite venture to take on Starlink", "TITLE\n'Wall Street Journal Tries “Recovery Finally Underway” Office Space Patter as Securitized Office Mortgage Delinquencies Hit a New Post-Crisis High of 10.4%, '\nDESCRIPTION\n', The Journal gets egg on its face for trying to call a bottom in the office space market even as delinquencies were accelerating", "TITLE\n'Nomura has space to cut a further $187 mln in costs, CEO says, '\nDESCRIPTION\n', NOMURA-CEO/ (PIX):Nomura has space to cut", "TITLE\n'Astronomers Pinpoint Origin Of Mysterious Repeating Radio Bursts From Space, '\nDESCRIPTION\n', Slowly repeating bursts of intense radio waves from space have puzzled astronomers since they were discovered in 2022.", "TITLE\n'As Satellites, Space Junk Crowd Earth Orbit, Global Push For Cooperation, '\nDESCRIPTION\n', The rapid increase in satellites and space junk will make low Earth orbit unusable unless companies and countries cooperate and share the data needed to manage that most accessible region of space, experts and industry insiders said.", "TITLE\n'This is a safe space: what's a really weird yet harmless habit you had as a kid?, '\nDESCRIPTION\n', You should've seen my rock collection.View Entire Post ›", 'TITLE\n\'T-Mobile and CrunchLabs will send your Google Pixel selfie to space, \'\nDESCRIPTION\n\', T-Mobile and CrunchLabs to launch "Space Selfies" in order to promote STEM education', "TITLE\n'India-USA Space and Geospatial Business Summit focus on tech & advanced manufacturing, '\nDESCRIPTION\n', The 4th India-USA Space and Geospatial Business Summit in Hyderabad focused on technology, policy alignment, and advanced manufacturing, aiming to boost bilateral trade in geospatial and space technologies. Highlighting India's potential as a global hub for c…", "TITLE\n'India nearing self-reliance in strategic navigation with NavIC: In-SPACe chief, '\nDESCRIPTION\n', India is nearly self-reliant in data for strategic applications due to NavIC, its satellite navigation system similar to GPS, according to In-SPACe Chairman Pawan Goenka. NavIC ensures independence for strategic needs and will coexist with other systems. Indi…", 
"TITLE\n'Disbursement of Rs 1,000 cr venture fund for space sector likely to begin in Q1 FY26: Pawan Goenka, '\nDESCRIPTION\n', IN-SPACe plans to make the first disbursal from the Rs 1000 crore venture capital fund to support space technology startups in the next financial year's first quarter. A fund manager will be selected through a SEBI process. The initiative aims to support appr…", "TITLE\n'The best wall-mounted space heater I've ever used is $20 off for Cyber Monday, '\nDESCRIPTION\n', If you're looking 
for an affordable heating solution for that chilly room in your home, the Dreo Smart Wall Heater is efficient and reliable, and it's on sale for Cyber Monday.", "TITLE\n'Trump may cancel Nasa’s powerful SLS Moon rocket – here’s what that would mean for Elon Musk and the future of space travel, '\nDESCRIPTION\n', The Space Launch System is a crucial part of America’s plans to return to the Moon.", "TITLE\n'Vacant Miami Retail Space? Good Luck Finding It., '\nDESCRIPTION\n', In Miami, even a retail miss can be a 
retail win. Take the Key Club.\xa0 The American bistro was on a busy corner in the heart of the coveted Coconut Grove neighborhood. The concept was also the brainchild of David Grutman, the king of Miami nightlife, who had l…", "TITLE\n'Extra Space Storage Provides Self-Storage Developer $41M Bridge Loan, '\nDESCRIPTION\n', For Extra Space Storage and self-storage developer 1784 Holdings, communication is key. The real estate investment trust has once again provided the developer with bridge financing tied to a storage facility in Southern California, this time lending $41.3 mil…", "TITLE\n'Global push for cooperation as space traffic crowds Earth's orbit, '\nDESCRIPTION\n', A United Nations panel on space traffic coordination called for a shared database of orbital objects as well as an international framework to track and manage them."]


'''
