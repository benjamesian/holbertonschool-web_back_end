import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()]).then(data => {
    const [photoData, userData] = data;
    console.log(photoData.body, userData.firstName, userData.lastName);
  }, _ => {
    console.log('Signup system offline');
  })
}
