export async function createKeyPair() {
    const keyPair = await window.crypto.subtle.generateKey(
        {
            'name': 'ECDH',
            'namedCurve': 'P-256'
        },
        true,
        ['deriveKey']
    )

    let publicKey = await window.crypto.subtle.exportKey('jwk', keyPair.publicKey)
    let privateKey = await window.crypto.subtle.exportKey('jwk', keyPair.privateKey)
    console.log(publicKey, privateKey)
    return {
        'publicKey': publicKey,
        'privateKey': privateKey
    }
}

async function importKeyfromJWK(jwk) {
    return await window.crypto.subtle.importKey(
        'jwk',
        jwk,
        {
            'name': 'ECDH',
            'namedCurve': 'P-256'
        },
        true,
        ['deriveKey']
    )
}


// Create a shared key using one's own privateKey and the other's publicKey
// Input privateKey and publicKey must be in JSON web key format
// Return the shared 
export async function createSharedKey(publicKey, privateKey) {

    let publicKey = await importKeyfromJWK(publicKey)
    let privateKey = await importKeyfromJWK(privateKey)
    return await window.crypto.subtle.deriveKey(
        {
            'name': 'ECDH',
            'public': publicKey
        },
        privateKey,
        {
            'name': 'AES-GCM',
            'length': 256
        },
        false,
        ['encrypt', 'decrypt']
    )
}