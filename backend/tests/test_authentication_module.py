from app.api.auth import _generate_otp


def test_generate_otp_is_six_digits():
    """Verify that authentication OTPs contain exactly 6 digits."""
    otp = _generate_otp()

    assert len(otp) == 6
    assert otp.isdigit()


def test_generate_otp_generates_new_codes():
    """Verify that OTP generation produces different codes."""
    otp1 = _generate_otp()
    otp2 = _generate_otp()
    assert otp1 != otp2