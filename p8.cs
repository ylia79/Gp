using UnityEngine;

public class SnowfallController : MonoBehaviour
{
    public ParticleSystem snowfallParticleSystem;
    public float snowfallIntensity = 100.0f;

    private ParticleSystem.EmissionModule emissionModule;

    private void Start()
    {
        if (snowfallParticleSystem != null)
        {
            emissionModule = snowfallParticleSystem.emission;
            emissionModule.rateOverTime = 0; // Initially, no snowfall
        }
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.S)) // You can change the input key as needed
        {
            ToggleSnowfall(); // Toggle snowfall on/off
        }
    }

    private void ToggleSnowfall()
    {
        if (emissionModule.enabled)
        {
            emissionModule.rateOverTime = 0; // Turn off snowfall
        }
        else
        {
            emissionModule.rateOverTime = snowfallIntensity; // Turn on snowfall
        }
    }
}
