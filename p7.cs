using UnityEngine;

public class CharacterController : MonoBehaviour
{
    public float moveSpeed = 5f;

    private Animator animator;

    private void Start()
    {
        animator = GetComponent<Animator>();
    }

    private void Update()
    {
        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");

        Vector3 movement = new Vector3(horizontalInput, verticalInput, 0);
        movement.Normalize();

        if (movement != Vector3.zero)
        {
            transform.Translate(movement * moveSpeed * Time.deltaTime);
            animator.SetFloat("Speed", 1);  // Trigger walking animation
        }
        else
        {
            animator.SetFloat("Speed", 0);  // Trigger idle animation
        }
    }
}
