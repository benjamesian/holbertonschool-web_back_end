import { uploadPhoto, createUser } from './utils'

export default async function asyncUploadUser() {
  const output = {
    photo: null,
    user: null,
  }
  return Promise.all([uploadPhoto(), createUser()]).then(data => {
    const [photoData, userData] = data;
    output.photo = photoData;
    output.user = userData;
  }).finally(() => output);
}
