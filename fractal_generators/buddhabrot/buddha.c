#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

// Size of the Image Canvas
#define HEIGHT 1000

#define ZOOM 0.4f
#define Y_PAN 0.0f
#define X_PAN -0.3f

// Range of the Complex Plane
#define MIN_X -2.0f + X_PAN + ZOOM
#define MAX_X 2.0f + X_PAN - ZOOM

#define MAX_Y 2.0f + Y_PAN - ZOOM
#define MIN_Y -2.0f + Y_PAN + ZOOM

// Max iterations till Zn
#define ITER 100000

// Save at every #of points picked
#define SAVE_COUNT 100000

int R_DATA[HEIGHT * HEIGHT] = {0};
int G_DATA[HEIGHT * HEIGHT] = {0};
int B_DATA[HEIGHT * HEIGHT] = {0};

float map_to_scale(float, float, float, float, float);
int get_array_loc(int, int);
float get_random(float, float);
void write_to_file();
int read_from_file();

int main()
{
    srand(time(NULL));

    // Counts how many points picked
    unsigned int POINTS_PICKED = 0;

    int s = read_from_file();

    while (1)
    {
        //pick a random point(a,b) in the canvas
        float pa = get_random(MIN_X, MAX_X);
        float pb = get_random(MAX_Y, MIN_Y);

        float a = pa;
        float b = pb;

        //original values
        float _a = a;
        float _b = b;

        unsigned int counter = 0;

        int bailout = 0;

        //calculate z^2 + c
        while (counter < ITER)
        {

            float aa = (a * a) - (b * b);
            float bb = 2 * a * b;

            a = aa + _a;
            b = bb + _b;

            if ((abs(aa + bb)) > 4)
            {
                bailout = 1;
                break;
            }

            counter += 1;
        }

        a = pa;
        b = pb;

        /*
        bailout is true
        point doesn't exist in set
        store points
        */
        if (bailout == 1)
        {
            counter = 0;

            while (counter < ITER)
            {
                float aa = (a * a) - (b * b);
                float bb = 2 * a * b;

                a = aa + _a;
                b = bb + _b;

                //if point escapes, stop
                if ((abs(aa + bb)) > 4)
                {
                    break;
                }

                //if point is within canvas range
                if (a > MIN_X && a < MAX_X && b < MAX_Y && b > MIN_Y)
                {
                    //mapping points to pixel scale
                    float _m = floor(map_to_scale(a, MIN_X, MAX_X, (float)0, (float)HEIGHT));
                    float _n = floor(map_to_scale(b, MAX_Y, MIN_Y, (float)0, (float)HEIGHT));

                    int m = (int)_m;
                    int n = (int)_n;

                    //blue 10-10000 iterations
                    //green is 10000-1000000
                    //red is 1000000-5000000

                    int l = get_array_loc(m, n);

                    if (counter > 10 && counter < 1000){
                        B_DATA[l] += 1;
                    }

                    if (counter > 1000 && counter < 20000){
                        G_DATA[l] += 1;
                    }

                    if (counter > 20000 && counter < 100000){
                        R_DATA[l] += 1;
                    }
                }

                counter = counter + 1;
            }
        }

        POINTS_PICKED += 1;

        //PRINT PROGRESS TO NEXT SAVE CHECKPOINT
        float multiple = SAVE_COUNT;
        float prec = multiple / 10;

        if (!((int)POINTS_PICKED % (int)prec))
        {
            int progress = ((((int)POINTS_PICKED % (int)multiple) * 1.0) / (int)multiple) * 100;
            printf(".");
        }

        //WRITE TO FILE
        if ((POINTS_PICKED % SAVE_COUNT) == 0)
        {
            write_to_file();
        }
    }
}

int read_from_file()
{
    FILE *r;
    FILE *g;
    FILE *b;

    r = fopen("r.txt", "r");
    g = fopen("g.txt", "r");
    b = fopen("b.txt", "r");

    //read file into array
    int i;
    if (r == NULL || g == NULL || b == NULL)
    {
        printf("Starting fresh.\n");
        return 0;
    }
    else
    {
        for (i = 0; i < (HEIGHT * HEIGHT); i++)
        {
            fscanf(r, "%d,", &R_DATA[i]);
            fscanf(g, "%d,", &G_DATA[i]);
            fscanf(b, "%d,", &B_DATA[i]);
        }
        fclose(r);
        fclose(g);
        fclose(b);

        printf("Starting from where I left off.\n");
    }
}

void write_to_file()
{

    FILE *fw;

    //Write Red
    fw = fopen("r.txt", "w");
    for (int i = 0; i < (HEIGHT * HEIGHT); i++)
    {
        fprintf(fw, "%d,", R_DATA[i]);
    }
    fclose(fw);

    //Write Green
    fw = fopen("g.txt", "w");
    for (int i = 0; i < (HEIGHT * HEIGHT); i++)
    {
        fprintf(fw, "%d,", G_DATA[i]);
    }
    fclose(fw);

    //Write Blue
    fw = fopen("b.txt", "w");
    for (int i = 0; i < (HEIGHT * HEIGHT); i++)
    {
        fprintf(fw, "%d,", B_DATA[i]);
    }
    fclose(fw);
}

float get_random(float min, float max)
{
    float r = ((float)rand() / (float)(RAND_MAX));
    float x = map_to_scale((float)r, 0.0f, 1.0f, min, max);
    return x;
}

float map_to_scale(float x, float in_min, float in_max, float out_min, float out_max)
{
    if (in_max == 0)
    {
        return 0;
    }
    else
    {
        return (((x - in_min) * (out_max - out_min)) / (in_max - in_min)) + out_min;
    }
}

//get location from co-ordinates to array index
int get_array_loc(int m, int n)
{
    return ((HEIGHT * n) + m);
}
