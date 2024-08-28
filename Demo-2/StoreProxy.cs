// Please reference ./CopilotPlayground-main/FollowStandards/PetProxy.cs

using System.Net;
using System.Net.Http;
using System.Net;
using System.Net.Http.Headers;

public class StoreProxy
{
    const string baseUrl = "https://petstore.swagger.io/v2";
    static HttpClient client = new HttpClient();
    // TestStoreProxy
    // Handle negative values
    

    static public async Task<string> GetOrder(int id)
    {
        string order = string.Empty;

        // Call rest api to get the user based on name
        HttpResponseMessage response = await client.GetAsync( $"{baseUrl}/store/order/{id}");
        // PetProxy
        // Handle the case where the response is not HTTP OK
    }
}
    







    


    
    