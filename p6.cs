using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraShake : MonoBehaviour
{
    // Duration and magnitude of the shake
    public float shakeDuration = 0.5f;
    public float shakeMagnitude = 0.1f;

    // Transform of the camera to shake
    private Transform cameraTransform;

    // Initial position of the camera
    private Vector3 initialPosition;

    void Start()
    {
        cameraTransform = GetComponent<Transform>();
        initialPosition = cameraTransform.localPosition;
    }

    public void Shake()
    {
        StartCoroutine(ShakeCoroutine());
    }

    private IEnumerator ShakeCoroutine()
    {
        float elapsed = 0.0f;

        while (elapsed < shakeDuration)
        {
            Vector3 randomPos = initialPosition + Random.insideUnitSphere * shakeMagnitude;

            cameraTransform.localPosition = randomPos;

            elapsed += Time.deltaTime;

            yield return null;
        }

        cameraTransform.localPosition = initialPosition;
    }
}
