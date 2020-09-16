export default function handleResponseFromAPI(promise) {
  return promise.then(_ => {
    console.log('Got a response from the API');
    return { status: 200, body: 'success' };
  }, _ => {
    console.log('Got a response from the API');
    return Error();
  });
}
