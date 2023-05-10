regions = [
    'Los Angeles, CA', 'New York, NY', 'Chicago, IL', 'Houston, TX', 'Phoenix, AZ',
    'Philadelphia, PA', 'San Antonio, TX', 'San Diego, CA', 'Dallas, TX', 'San Jose, CA',
    'Austin, TX', 'Jacksonville, FL', 'Fort Worth, TX', 'Columbus, OH', 'Charlotte, NC',
    'San Francisco, CA', 'Indianapolis, IN', 'Seattle, WA', 'Denver, CO', 'Washington, DC',
    'Boston, MA', 'El Paso, TX', 'Nashville, TN', 'Detroit, MI', 'Portland, OR', 'Memphis, TN',
    'Oklahoma City, OK', 'Las Vegas, NV', 'Louisville, KY', 'Baltimore, MD', 'Milwaukee, WI',
    'Albuquerque, NM', 'Tucson, AZ', 'Fresno, CA', 'Mesa, AZ', 'Sacramento, CA', 'Atlanta, GA',
    'Kansas City, MO', 'Colorado Springs, CO', 'Miami, FL', 'Raleigh, NC', 'Omaha, NE',
    'Long Beach, CA', 'Virginia Beach, VA', 'Oakland, CA', 'Minneapolis, MN', 'Tulsa, OK',
    'Tampa, FL', 'Arlington, TX', 'New Orleans, LA', 'Wichita, KS', 'Cleveland, OH', 'Seattle, WA',
    'Santa Ana, CA', 'Riverside, CA', 'Corpus Christi, TX', 'Lexington, KY', 'Stockton, CA',
    'Henderson, NV', 'Saint Paul, MN', 'St. Louis, MO', 'Cincinnati, OH', 'Pittsburgh, PA',
    'Greensboro, NC', 'Anchorage, AK', 'Plano, TX', 'Lincoln, NE', 'Orlando, FL', 'Irvine, CA',
    'Newark, NJ', 'Durham, NC', 'Chula Vista, CA', 'Toledo, OH', 'Fort Wayne, IN', 'St. Petersburg, FL',
    'Laredo, TX', 'Jersey City, NJ', 'Chandler, AZ', 'Madison, WI', 'Lubbock, TX', 'Scottsdale, AZ',
    'Reno, NV', 'Buffalo, NY', 'Gilbert, AZ', 'Glendale, AZ', 'North Las Vegas, NV', 'Winston–Salem, NC',
    'Chesapeake, VA', 'Norfolk, VA', 'Fremont, CA', 'Garland, TX', 'Irving, TX', 'Hialeah, FL',
    'Richmond, VA', 'Boise, ID', 'Spokane, WA', 'Baton Rouge, LA', 'Tacoma, WA', 'San Bernardino, CA',
    'Modesto, CA', 'Fontana, CA', 'Des Moines, IA', 'Moreno Valley, CA', 'Santa Clarita, CA',
    'Fayetteville, NC', 'Birmingham, AL', 'Oxnard, CA', 'Rochester, NY', 'Port St. Lucie, FL',
    'Grand Rapids, MI', 'Huntsville, AL', 'Salt Lake City, UT', 'Frisco, TX', 'Yonkers, NY',
    'Amarillo, TX', 'Glendale, CA', 'Huntington Beach, CA', 'McKinney, TX', 'Montgomery, AL',
    'Augusta, GA', 'Aurora, IL', 'Akron, OH', 'Little Rock, AR', 'Tempe, AZ', 'Columbus, GA',
    'Overland Park, KS', 'Grand Prairie, TX', 'Tallahassee, FL', 'Cape Coral, FL', 'Mobile, AL',
    'Knoxville, TN', 'Shreveport, LA', 'Worcester, MA', 'Ontario, CA', 'Vancouver, WA', 'Sioux Falls, SD',
    'Chattanooga, TN', 'Brownsville, TX', 'Fort Lauderdale, FL', 'Providence, RI', 'Newport News, VA',
    'Rancho Cucamonga, CA', 'Santa Rosa, CA', 'Peoria, AZ', 'Oceanside, CA', 'Elk Grove, CA',
    'Salem, OR', 'Pembroke Pines, FL', 'Eugene, OR', 'Garden Grove, CA', 'Cary, NC', 'Fort Collins, CO',
    'Corona, CA', 'Springfield, MO', 'Jackson, MS', 'Alexandria, VA', 'Hayward, CA', 'Clarksville, TN',
    'Lakewood, CO', 'Lancaster, CA', 'Salinas, CA', 'Palmdale, CA', 'Hollywood, FL', 'Springfield, MA',
    'Macon, GA', 'Kansas City, KS', 'Sunnyvale, CA', 'Pomona, CA', 'Killeen, TX', 'Escondido, CA',
    'Pasadena, TX', 'Naperville, IL', 'Bellevue, WA', 'Joliet, IL', 'Murrieta, CA', 'Midland, TX',
    'Rockford, IL', 'Paterson, NJ', 'Savannah, GA', 'Bridgeport, CT', 'Torrance, CA', 'McAllen, TX',
    'Syracuse, NY', 'Surprise, AZ', 'Denton, TX', 'Roseville, CA', 'Thornton, CO', 'Miramar, FL',
    'Pasadena, CA', 'Mesquite, TX', 'Olathe, KS', 'Dayton, OH', 'Carrollton, TX', 'Waco, TX',
    'Orange, CA', 'Fullerton, CA', 'Charleston, SC', 'West Valley City, UT', 'Visalia, CA',
    'Hampton, VA', 'Gainesville, FL', 'Warren, MI', 'Coral Springs, FL', 'Cedar Rapids, IA',
    'Round Rock, TX', 'Sterling Heights, MI', 'Kent, WA', 'Columbia, SC', 'Santa Clara, CA',
    'New Haven, CT', 'Stamford, CT', 'Concord, CA', 'Elizabeth, NJ', 'Athens, GA', 'Thousand Oaks, CA',
    'Lafayette, LA', 'Simi Valley, CA', 'Topeka, KS', 'Norman, OK', 'Fargo, ND', 'Wilmington, NC',
    'Abilene, TX', 'Odessa, TX', 'Columbia, MO', 'Pearland, TX', 'Victorville, CA', 'Hartford, CT',
    'Vallejo, CA', 'Allentown, PA', 'Berkeley, CA', 'Richardson, TX', 'Arvada, CO', 'Ann Arbor, MI',
    'Rochester, MN', 'Cambridge, MA', 'Sugar Land, TX', 'Lansing, MI', 'Evansville, IN', 'College Station, TX',
    'Fairfield, CA', 'Clearwater, FL', 'Beaumont, TX', 'Independence, MO', 'Provo, UT', 'West Jordan, UT',
    'Murfreesboro, TN', 'Palm Bay, FL', 'El Monte, CA', 'Carlsbad, CA', 'North Charleston, SC',
    'Temecula, CA', 'Clovis, CA', 'Springfield, IL', 'Meridian, ID', 'Westminster, CO', 'Costa Mesa, CA',
    'High Point, NC', 'Manchester, NH', 'Pueblo, CO', 'Lakeland, FL', 'Pompano Beach, FL', 'West Palm Beach, FL',
    'Antioch, CA', 'Everett, WA', 'Downey, CA', 'Lowell, MA', 'Centennial, CO', 'Elgin, IL', 'Richmond, CA',
    'Peoria, IL', 'Broken Arrow, OK', 'Miami Gardens, FL', 'Billings, MT', 'Jurupa Valley, CA', 'Sandy Springs, GA',
    'Gresham, OR', 'Lewisville, TX', 'Hillsboro, OR', 'Ventura, CA', 'Greeley, CO', 'Inglewood, CA', 'Waterbury, CT',
    'League City, TX', 'Santa Maria, CA', 'Tyler, TX', 'Davie, FL', 'Lakewood, CA', 'Boulder, CO', 'Allen, TX',
    'West Covina, CA', 'Sparks, NV', 'Wichita Falls, TX', 'Green Bay, WI', 'San Mateo, CA', 'Norwalk, CA',
    'Rialto, CA', 'Las Cruces, NM', 'Chico, CA', 'El Cajon, CA', 'Burbank, CA', 'South Bend, IN', 'Renton, WA',
    'Vista, CA', 'Davenport, IA', 'Edinburg, TX', 'Tuscaloosa, AL', 'Carmel, IN', 'Spokane Valley, WA',
    'San Angelo, TX', 'Vacaville, CA', 'Clinton, MI', 'Bend, OR', 'Woodbridge, NJ', 'Lakewood, NJ',
    'San Leandro, CA', 'Santa Barbara, CA', 'Kenosha, WI', 'Greeley, CO', 'South Gate, CA', 'Mission Viejo, CA',
    'Lawrence, KS', 'Duluth, MN', 'Lawton, OK', 'Gary, IN', 'Menifee, CA', 'Pleasanton, CA', 'Carmel, IN',
    'Lodi, CA', 'Perris, CA', 'San Marcos, CA', 'Cupertino, CA', 'Lake Forest, CA', 'Tustin, CA', 'Meridian, ID',
    'Mountain View, CA', 'Dothan, AL', 'Pico Rivera, CA', 'Montebello, CA', 'Lodi, CA', 'New Braunfels, TX',
    'Marysville, WA', 'Tamarac, FL', 'Madera, CA', 'Conroe, TX', 'Santa Cruz, CA', 'Eden Prairie, MN',
    ]