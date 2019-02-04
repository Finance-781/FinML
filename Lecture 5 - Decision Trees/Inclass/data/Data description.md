

<H2>Data description</H2>
<H3>Data dictionary</H3>

| Variable             | Definition                                               | Key           |
|----------------------|----------------------------------------------------------|---------------|
| company_id           | Company ID                                               |               |
| category_code        | Company category                                         |               |
| country_code         | Country                                                  | USA, NZL, other|
| state_code           | State                                                    | California, other |
| ipo                  | IPO                                                      | True or False |
| is_acquired          | Company is acquired or not                               | True or False |
| is_closed            | Company is closed or not                                 | True or False |
| age                  | Company age in days                                      |               |
| mba_degree           | Number of people with MBA degree associated with company |               |
| phd_degree           | Number of people with PhD degree associated with company |               |
| ms_degree            | Number of people with MS degree associated with company  |               |
| other_degree         | Number of other people associated with company           |               |
| offices              | Number of company's offices                              |               |
| average_funded       | Funds per round                                          |               |
| average_participants | Participants per round                                   |               |
| total_rounds         | Total number of rounds                                   |               |
| products_number      | Total number of products                                 |               |
| acquired_companies   | Total number of acquired companies                       |               |

<H3>Variable notes</H3>
<H4>Age</H4>
Age is calculated by next rule: if company is acquired, then age is set up on acquiring date, else on 01.01.2014.
