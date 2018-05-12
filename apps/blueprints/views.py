from django.http import HttpResponse



def index(request):
    return HttpResponse('It works!')


# from django.shortcuts import render

# from web3 import Web3, HTTPProvider

# from .abi_defs import factoryAbi, mintAbi, factoryAddress, mintAddress, blueprintAbi

# mintAddress = "0xfD69413a26b451fdAA8b51FbeE1581752B9F745F"
# masterAddress = "0xA3A4435aE1e025E184FfC80763D30Ea55a8C9372"

# contractOwner = "0x002aF9F9CB3fE3416881fD63C183826C6e59ad45"

# infuraTestURL = 'https://ropsten.infura.io/Ke3AtZSlNpKtZEJz6JQR'

# HARDCODED_USER_WALLET = "0x106F9774c34773a3d1827ead1195d6B737e3f443"

# def index(request):
#     return render(request, 'blueprints/index.html')

# def createablueprint(request):
#     return render(request, 'blueprints/createablueprint.html')

# def instructions(request):
#     return render(request, 'blueprints/instructions.html')

# def myblueprints(request):
#     web3 = Web3(HTTPProvider(infuraTestURL))
#     mintContract = web3.eth.contract(address = mintAddress, abi = mintAbi)
#     factoryContract = web3.eth.contract(address = factoryAddress, abi = factoryAbi)

#     blueprintList = []

#     noOfBlueprints = factoryContract.functions.noOfBlueprints().call()

#     for n in range (1,noOfBlueprints+1):
        
#         address,ticker,margin,expirationTime,creationTime,creatorID,creatorAddress = factoryContract.functions.lookupBlueprintMeta(n).call()

#         print(margin)


#         if (address != "0x0000000000000000000000000000000000000000"):
#             #blueprintAddress = blueprint[0]
#             #blueprintContract = web3.eth.contract(address = blueprintAddress, abi = blueprintAbi)

#             entryPrice = 0
#             exitPrice = 0

#             blueprintID = n
            
            
#             blueprintList.append(blueprints(blueprintID,address,ticker,margin,expirationTime,creationTime,creatorID,creatorAddress,entryPrice,exitPrice))

#     print (blueprintList) 
#     #event_filter = factoryContract.eventFilter('BlueprintCreated')
#     #print (event_filter.getFilterLogs())

    

#     return render(request, 'blueprints/myblueprints.html', {"blueprintList": blueprintList})

# def purchasedblueprints(request):
#     return render(request, 'blueprints/purchasedblueprints.html')

# def blueprintsubmissionconfirmation(request):
#     return render(request, 'blueprints/blueprintsubmissionconfirmation.html')
#     
