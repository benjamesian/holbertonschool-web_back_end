export default function createReportObject(employeesList) {
  return {
    allEmployees: [...employeesList],
    getNumberofDepartments(employeesList) {
      return Object.keys(employeesList).length
    }
  }
}
