if __name__ == "__main__":

    from twilio.rest import Client 

    account_sid = 'ACea84a60986ac9e3d526ad3796e3cbde5' 
    auth_token = 'ac5c96f1947752b4424637e49210b51f' 
    client = Client(account_sid, auth_token) 

    Sam = '+13162073470'
    Siew = '+17203699588'
    Erick = '+12108655122'
    Media = []
    #Media = 'https://media.giphy.com/media/L13NsH0Aij4Sf2Gdjt/source.gif'
    message = ''
    #message = 'How you doin'
    recipiant = Sam

    message = client.messages.create( 
                                from_ ='+18305634753',  
                                body ='-\n' + message,      
                                to = recipiant,
                                media_url = Media
                                    ) 

    print(f"Created a new message: {message.sid}")
#%%
for sms in client.messages.list():
    print(sms.to)
#%% Auxilary Notes
#Curl command for post
'''
curl "https://api.twilio.com/2010-04-01/Accounts/ACea84a60986ac9e3d526ad3796e3cbde5/Messages.json" -X POST --data-urlencode "To=+13162073470" --data-urlencode "From=+18305634753" --data-urlencode "Body=This is by body" -u ACea84a60986ac9e3d526ad3796e3cbde5:ac5c96f1947752b4424637e49210b51f
'''
#Curl command for get
'''
curl "https://api.twilio.com/2010-04-01/Accounts/ACea84a60986ac9e3d526ad3796e3cbde5/Messages.json" -X GET -u ACea84a60986ac9e3d526ad3796e3cbde5:ac5c96f1947752b4424637e49210b51f
'''

#Program the reciever API:
# If you recieve a text from me, follow the pretty formating
# If you recieve a textt from someone else, send it to me. 

'''
I send a message to the app with the format


Contact:
Time:
Body:
Gif: 


The app will read the message, and use twilio to receive the data into python, python to format the message, set the delay, and twilio to send the message to the user. 


A confirmation message would be nice too. 


Gifs 
Morning kiss 
https://giphy.com/gifs/love-couple-bae-cEao6F6uvHPCE


https://giphy.com/gifs/bed-kisses-cuddles-A8O8nTI7TtbvG


https://giphy.com/gifs/love-black-and-white-UiedAqB76nife


https://giphy.com/gifs/memecandy-ZZlghJOkbtZvbBrN4p


https://giphy.com/gifs/ycbcn1ee0UCsw


https://giphy.com/gifs/john-stamos-fuller-house-lori-loughlin-SEsCdoVfZa5W0


Funny/cute: 


https://giphy.com/gifs/kiss-90s-baby-dpSrm4cwUmCeQ


https://giphy.com/gifs/kiss-90s-baby-dpSrm4cwUmCeQ


https://giphy.com/gifs/cute-glass-mice-tCWMUAuZLMvKg


https://giphy.com/gifs/minion-kiss-l2Jhok92mZ2PZHjDG


https://giphy.com/gifs/90s-mr-bean-Nydo55HzhyGqI


https://giphy.com/gifs/l0EoAl1ECVSSWuwr6


https://giphy.com/gifs/love-i-you-that-70s-show-2dQ3FMaMFccpi


https://giphy.com/gifs/memecandy-iJguNBUR9pTYfITTeW


https://giphy.com/gifs/tanamongeau-funny-friends-xUOxeSoXTMO9H7a93y


Romantic 
https://giphy.com/gifs/love-movie-dCFwyvRTMeSfm


https://giphy.com/gifs/perfect-reasons-DTXugNB5Jt6Ra


https://giphy.com/gifs/ryan-gosling-thenotebookedit-rosamundpike-3wB3QcqXDMt20


https://giphy.com/gifs/disneypixar-disney-pixar-8FbmKNAAw92tW


Sensual: 
https://giphy.com/gifs/kiss-movie-ryan-gosling-HN4Om0tu8y7gk 


https://giphy.com/gifs/syfy-bitten-werewolves-syfy-3o6ozHbQHZzDTxRjsA


Climbing:
https://giphy.com/gifs/spidermanhomecoming-spiderman-homecoming-xT9IgvthjO6xWlGF1u


https://giphy.com/gifs/iprlQKfz9ScvI6Lqph


https://giphy.com/gifs/dinosaur-climbing-good-luck-4kNNAtKDm2HRe


https://giphy.com/gifs/dinosaur-climbing-good-luck-4kNNAtKDm2HRe


https://giphy.com/gifs/rock-bear-climbing-lG5FxBIU4dFRK


Notice me: 


https://giphy.com/gifs/conan-obrien-3o6gb3kkXfLvdKEZs4


https://giphy.com/gifs/snl-saturday-night-live-2010s-26ufeTcolY1CMlAvm


https://giphy.com/gifs/hyperrpg-rat-queens-ratqueensrpg-ratqueens-KZhMX8YXdD8kZ4JDFq


https://giphy.com/gifs/partydownsouth-party-down-south-cmt-xTk9ZYrrME45cvEPMA


https://giphy.com/gifs/tanamongeau-funny-friends-xUOxeSoXTMO9H7a93y


https://giphy.com/gifs/needy-love-FfjQU0sO2zP5S


https://giphy.com/gifs/needy-love-FfjQU0sO2zP5S


Greys anatomy 
https://giphy.com/gifs/abcnetwork-DxwthvKPpk1e8


https://giphy.com/gifs/documentary-now-nUZ3YuL0RAOyc


https://giphy.com/gifs/greys-anatomy-cristina-yang-gareTUclVKANi


https://giphy.com/gifs/greys-anatomy-cristina-yang-gareTUclVKANi


https://giphy.com/gifs/reaction-greys-anatomy-cristina-yang-oRIhcOBB9GVC8


https://giphy.com/gifs/home-greys-anatomy-no-food-46qQ44dqV93I4


https://giphy.com/gifs/people-LhoIGi2uye2ze


https://giphy.com/gifs/greys-anatomy-alex-karev-3ohhwHHQd3ISVQvoJi


https://giphy.com/gifs/greys-anatomy-derek-shepherd-lexie-grey-2lRzZBmRAxEME






https://giphy.com/gifs/SkyTV-weird-greys-anatomy-skywitness-1fkdaiYSkzKGM2a3Wj
'''