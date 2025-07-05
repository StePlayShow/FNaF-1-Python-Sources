#version 330 core

in vec2 fragmentTexCoord;

out vec4 color;
uniform sampler2D imageTexture;

void main()
{
    vec2 coordinates;
    float pixelDistanceX;
    float pixelDistanceY;
    float offset;
    float dir;

    pixelDistanceX = distance(fragmentTexCoord.x, 0.5);
    pixelDistanceY = distance(fragmentTexCoord.y, 0.5);

    offset = (pixelDistanceX*0.2) * pixelDistanceY;

    if (fragmentTexCoord.y <= 0.5)
        dir = 1.0;
    else
        dir = -1.0;

    coordinates = vec2(fragmentTexCoord.x, fragmentTexCoord.y + pixelDistanceX*(offset*8.0*dir));

    color = vec4(texture(imageTexture, coordinates).rgb, 1.0);
}