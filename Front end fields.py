# FRONT END input
#his is the input of front end fields
#coming from the answers provided by the user in the website

# all data inputs values  from the client are inserted into a field
# that belongs to one list
# the client input data is inserted in parameters that are part of a list.
# a list can be an element of another list. .


Hauptmieter = [Name,Street,Postcode,City,Country,DateofBirth,CityofBirth]
Untermieter = [Name,Street,Postcode,City,Country,DateofBirth,CityofBirth]

Mietobjekt = [Location,Description]
Description = [NumRooms,NumBathrooms,Kitchen,Livingroom,Balcony,Livingroom,Terrase,other]
Mietklauseln = [WhatRenttype,TermTime,TermStart,TermEnd,Rent,Furnished,PersonalFamily,other,KautionAmount]
Rent = [Miete,Nebenkosten]
Nebenkosten = [Gas,Heizung,Internet,Phone,Water]
Rentpayment = [Iban,Accountholder,Bankname]
Keyhandover = [Apartment,Building,Keller,Attic,Postbox]


# Clause Dictionaries
# the contract is written in many sentences.
# There is one dictionary for every language
# each clause is a dictionary key

EN_text = {'Key_a':'value_a'}
DE_text = {'Key_a':'value_a'}

#Contract Name
EN_text ['Titel_Contract_name'] = 'Sublease Contract'
DE_text ['Titel_Contract_name'] = 'Untermietvertrag'

#Zwischen
EN_text ['contract_between'] = 'between'
DE_text ['contract_between'] = 'zwischen'

#parties as...
EN_text ['parties_def_landlord'] = '("Sublessor")'
DE_text ['parties_def_landlord'] = '-Hauptmieter-'

#lease has been agreed
EN_text ['lease_agreed'] = 'the following residential sublease contract of residential space has been agreed upon:'
DE_text ['lease_agreed'] = 'kommt nachfolgender Untermietvertrag über Wohnraum zustande:'

#Clause Title §1  Leased Space
EN_text ['Titel_Mietraum'] = 'the following residential sublease contract of residential space has been agreed upon:'
DE_text ['Titel_Mietraum'] = 'kommt nachfolgender Untermietvertrag über Wohnraum zustande:'

#Mietraum definition
EN_text ['Mietraum'] = 'The Sublessor leases the Sublessee, for residential purposes,'
DE_text ['Mietraum'] = 'Der Hauptmieter vermietet dem Untermieter zu Wohnzwecken'
