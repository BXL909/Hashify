def is_it_in_tuple(tuple, thing_to_search):
    for each_hash in tuple:
        if each_hash == thing_to_search:
            return True
    return False 

def hash_it(thing_to_be_hashed,type_of_hash_wanted):
    import hashlib

    #validate type_of_hash_wanted
    if is_it_in_tuple(hashlib.algorithms_available, type_of_hash_wanted):
        #convert to bytes
        byte_encoded_thing_to_be_hashed = thing_to_be_hashed.encode()
        #construct the function name e.g hashlib.sha256(thingtobehashed) and call it. This is to avoid a massive IF statement.. 
        # e.g if sha256 then hashlib.sha256(blah). if sha384 then hashlib.sha384blahblah, etc.
        hashed_result = eval("hashlib." + type_of_hash_wanted)(byte_encoded_thing_to_be_hashed)
        #construct a list to return to the calling code
        print(type_of_hash_wanted)
        hashed_list = [str(hashed_result.hexdigest()), str(hashed_result.digest_size), str(hashed_result.block_size)]
        return hashed_list
    else:
        print ("Invalid selection")


